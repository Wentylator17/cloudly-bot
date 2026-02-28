import discord
from discord.ext import commands
from discord import ui

# --- Ustawienia bota ---
intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.members = True
bot = commands.Bot(command_prefix="!", intents=intents)

# --- Weryfikacja Button ---
class VerifyButton(ui.View):
    def __init__(self):
        super().__init__(timeout=None)  # timeout=None = przycisk nie wygasa

    @ui.button(label="Zweryfikuj się", style=discord.ButtonStyle.green, emoji="✅")
    async def verify(self, interaction: discord.Interaction, button: ui.Button):
        guild = interaction.guild
        member = interaction.user
        role = discord.utils.get(guild.roles, name="Zweryfikowany")  # nazwa roli

        if role:
            await member.add_roles(role)
            await interaction.response.send_message(
                "🎉 Pomyślnie zweryfikowano!", ephemeral=True
            )
        else:
            await interaction.response.send_message(
                "❌ Rola 'Zweryfikowany' nie istnieje! Utwórz ją najpierw.", ephemeral=True
            )

# --- Komenda wysyłająca embed weryfikacyjny ---
@bot.command()
async def weryfikacja(ctx):
    embed = discord.Embed(
        title="CloudlyHUB Weryfikacja",
        description="• Witaj w Cloudly Hub\n• Kliknij przycisk poniżej, aby się zweryfikować\n• Dziękujemy za wybranie naszych usług",
        color=discord.Color.blue()
    )
    embed.set_thumbnail(url="https://i.imgur.com/your_image.png")  # URL obrazka w prawym górnym rogu

    view = VerifyButton()
    await ctx.send(embed=embed, view=view)

# --- Event ready ---
@bot.event
async def on_ready():
    print(f'Zalogowano jako {bot.user}')

# --- Uruchomienie bota ---
import os
TOKEN = os.environ.get("TOKEN")
bot.run(TOKEN)
