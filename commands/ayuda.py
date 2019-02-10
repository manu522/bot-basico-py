import discord
async def run(message, args, utilidad):
    embed = discord.Embed(title="Ayuda", description="Lista de todos los comandos Disponibles", color=0x00ff00)
    for cmds in utilidad:
        embed.add_field(name=cmds['nombre'], value= '`Descripción`: ' + cmds['des'] + '\n`Uso`: ' + cmds['uso'], inline=False)
    await message.channel.send(embed=embed)


info = {
   "nombre": "ayuda",
   "des": "Te muestra todos los comandos disponibles",
   "uso": "<prefijo>ayuda"
}