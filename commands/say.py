async def run(message, args, utilidad):
   await message.channel.send(" ".join(args))
   await message.delete()


info ={
   "nombre": "say",
   "des": "El bot repite lo que le dices",
   "uso": "<prefijo>say [texto]"
}