import json
import os
import smtplib
import ssl
import urllib.request
from email.message import EmailMessage

def configured():
    channels=[]
    if os.getenv('TELEGRAM_BOT_TOKEN') and os.getenv('TELEGRAM_CHAT_ID'):channels.append('telegram')
    if all(os.getenv(k) for k in ('SMTP_HOST','SMTP_USER','SMTP_PASSWORD','NOTIFY_EMAIL')):channels.append('email')
    return channels

def send(channel,message):
    if channel=='telegram':
        url='https://api.telegram.org/bot'+os.environ['TELEGRAM_BOT_TOKEN']+'/sendMessage'
        payload=json.dumps({'chat_id':os.environ['TELEGRAM_CHAT_ID'],'text':message[:3900]}).encode()
        req=urllib.request.Request(url,data=payload,headers={'Content-Type':'application/json'})
        with urllib.request.urlopen(req,timeout=20) as r:
            if not json.load(r).get('ok'):raise RuntimeError('Telegram recusou envio')
    else:
        msg=EmailMessage();msg['Subject']='OMNIA Treasure Hunter — mudança detectada';msg['From']=os.environ['SMTP_USER'];msg['To']=os.environ['NOTIFY_EMAIL'];msg.set_content(message)
        with smtplib.SMTP_SSL(os.environ['SMTP_HOST'],int(os.getenv('SMTP_PORT','465')),context=ssl.create_default_context(),timeout=20) as smtp:
            smtp.login(os.environ['SMTP_USER'],os.environ['SMTP_PASSWORD']);smtp.send_message(msg)

def deliver(store,sender=send,channels=None):
    channels=configured() if channels is None else channels
    if not channels:return {'configured':False,'sent':0,'errors':0}
    count=errors=0
    for key,payload,done in store.db.execute('SELECT id,payload,channels FROM outbox WHERE sent=0').fetchall():
        r=json.loads(payload);done=json.loads(done)
        # Balance and coverage changes stay in report; financial opportunity alerts only.
        if r['category'] not in ('recompensa','bounty','recuperacao'):
            store.db.execute('UPDATE outbox SET sent=1 WHERE id=?',(key,));continue
        for channel in channels:
            if channel in done:continue
            try:
                sender(channel,f"{r['status']}: {r['title']}\nRede: {r['network']}\nQuantidade: {r.get('amount')} {r.get('asset')}\nValor anunciado: {r.get('announced_value')}\n{r.get('source','')}\nNão é confirmação de pagamento.")
                done.append(channel);count+=1
                store.db.execute('UPDATE outbox SET channels=? WHERE id=?',(json.dumps(done),key));store.db.commit()
            except Exception:
                # Never log exception strings containing Telegram tokens or SMTP credentials.
                errors+=1;print(json.dumps({'event':'notification_error','channel':channel,'id':key}))
        if all(ch in done for ch in channels):store.db.execute('UPDATE outbox SET sent=1 WHERE id=?',(key,))
    store.db.commit();return {'configured':True,'sent':count,'errors':errors}
