import discord
from discord import app_commands
from discord.ui import View, Button
import asyncio
import json
import os

TOKEN = ""
PROTECTED_SERVER_ID = # server id protectd
INVITE_LINK = ""
SPACE_BLOCK = "‎\n‎\n‎\n‎\n‎\n"

MSG1 = """# BOOM.⋆♱ BOOM.⋆♱  BOOM.⋆♱  BOOM.⋆♱  BOOM.⋆♱  BOOM.⋆♱  BOOM.⋆♱  BOOM.⋆♱  BOOM.⋆♱  BOOM.⋆♱  BOOM.⋆♱ [.](https://tenor.com/view/miguelillorl-king-nasir-dance-randomlife-zapatos-una-cosita-gif-1945223208845987384) [.](https://tenor.com/view/epstein-epstein-files-epstein-island-jeffrey-epstein-trump-epstein-gif-147873707617354730) [.](link your server)) BOOM.⋆♱ BOOM.⋆♱  BOOM.⋆♱  BOOM.⋆♱  BOOM.⋆♱  BOOM.⋆rière  BOOM.⋆rière  BOOM.⋆rière  BOOM.⋆rière  BOOM.⋆rière BOOM.⋆rière BOOM.⋆rière  BOOM.⋆rière  BOOM.⋆rière  BOOM.⋆rière  BOOM.⋆rière  BOOM.⋆rière  BOOM.⋆rière  BOOM.⋆rière  BOOM.⋆rière BOOM.⋆rière BOOM.⋆reira  BOOM.⋆reira  BOOM.⋆reira  BOOM.⋆reira  BOOM.⋆reira  BOOM.⋆reira  BOOM.⋆reira  BOOM.⋆reira"""

LANGUAGES = {
    "pt": {
        "title": "Legião Panel",
        "description": "Olá {mention}, Bem-vindo ao **Legião Bot**.\nEste painel é para spammar servidores sem controle.",
        "basic_spam": "Basic Spam",
        "clear_chat": "Limpar Chat",
        "access_denied": "Acesso Negado",
        "need_server": "Você precisa estar no servidor oficial para usar este painel."
    },
    "en": {
        "title": "Legião Panel",
        "description": "Hello {mention}, Welcome to **Legião Bot**.\nThis panel is for spamming servers without control.",
        "basic_spam": "Basic Spam",
        "clear_chat": "Clear Chat",
        "access_denied": "Access Denied",
        "need_server": "You need to be in the official server to use this panel."
    },
    "ru": {
        "title": "Панель Легиона",
        "description": "Привет {mention}, Добро пожаловать в **Legião Bot**.\nЭта панель для спама серверов без контроля.",
        "basic_spam": "Basic Spam",
        "clear_chat": "Очистить чат",
        "access_denied": "Доступ Запрещен",
        "need_server": "Вам нужно быть на официальном сервере, чтобы использовать эту панель."
    }
}

USER_DATA_FILE = "usuarios.json"

def load_user_data():
    if os.path.exists(USER_DATA_FILE):
        try:
            with open(USER_DATA_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except:
            return {}
    return {}

def save_user_data(data):
    with open(USER_DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def get_user_language(user_id):
    data = load_user_data()
    return data.get(str(user_id))

def set_user_language(user_id, lang):
    data = load_user_data()
    data[str(user_id)] = lang
    save_user_data(data)

class LegiaoView(View):
    def __init__(self, lang="pt"):
        super().__init__(timeout=None)
        self.lang = lang
        self.trans = LANGUAGES.get(lang, LANGUAGES["pt"])
        self.add_item(Button(label=self.trans["basic_spam"], style=discord.ButtonStyle.secondary, custom_id="basic_spam"))
        self.add_item(Button(label=self.trans["clear_chat"], style=discord.ButtonStyle.secondary, custom_id="clear_chat"))

    async def safe_send(self, interaction: discord.Interaction, content: str):
        for _ in range(8):
            try:
                await interaction.followup.send(content)
                return True
            except discord.HTTPException as e:
                if e.code == 40094:
                    return False
                if e.status == 429:
                    retry = getattr(e, 'retry_after', 1.5)
                    await asyncio.sleep(min(retry, 8))
                    continue
                await asyncio.sleep(0.8)
        return False

    async def basic_spam(self, interaction: discord.Interaction):
        await interaction.response.defer(ephemeral=True)
        for _ in range(5):
            if not await self.safe_send(interaction, MSG1):
                break
            await asyncio.sleep(0.3)

    async def clear_chat(self, interaction: discord.Interaction):
        await interaction.response.defer(ephemeral=True)
        for _ in range(5):
            if not await self.safe_send(interaction, SPACE_BLOCK * 120):
                break
            await asyncio.sleep(0.3)

    async def interaction_check(self, interaction: discord.Interaction) -> bool:
        if interaction.data["custom_id"] == "basic_spam":
            await self.basic_spam(interaction)
        elif interaction.data["custom_id"] == "clear_chat":
            await self.clear_chat(interaction)
        return True

class LanguageSelectView(View):
    def __init__(self, is_access_denied=False):
        super().__init__(timeout=None)
        self.is_access_denied = is_access_denied

    @discord.ui.button(label="Português", style=discord.ButtonStyle.primary, custom_id="lang_pt")
    async def pt_button(self, interaction: discord.Interaction, button: Button):
        await self.select_language(interaction, "pt")

    @discord.ui.button(label="English", style=discord.ButtonStyle.primary, custom_id="lang_en")
    async def en_button(self, interaction: discord.Interaction, button: Button):
        await self.select_language(interaction, "en")

    @discord.ui.button(label="Русский", style=discord.ButtonStyle.primary, custom_id="lang_ru")
    async def ru_button(self, interaction: discord.Interaction, button: Button):
        await self.select_language(interaction, "ru")

    async def select_language(self, interaction: discord.Interaction, lang: str):
        set_user_language(interaction.user.id, lang)
        await interaction.response.defer(ephemeral=True)
        try:
            await interaction.delete_original_response()
        except:
            pass
        trans = LANGUAGES.get(lang, LANGUAGES["pt"])
        if self.is_access_denied:
            embed = discord.Embed(title=trans["access_denied"], description=trans["need_server"], color=0x000000)
            view = InviteView()
            await interaction.followup.send(embed=embed, view=view, ephemeral=True)
        else:
            embed = discord.Embed(title=trans["title"], description=trans["description"].format(mention=interaction.user.mention), color=0x000000)
            embed.set_author(name="Legião Bot")
            view = LegiaoView(lang=lang)
            await interaction.followup.send(embed=embed, view=view, ephemeral=True)

class InviteView(View):
    def __init__(self):
        super().__init__(timeout=None)
        self.add_item(Button(label="Join Server", style=discord.ButtonStyle.link, url=INVITE_LINK))

class Client(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.all())
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        await self.tree.sync()

client = Client()

@client.tree.command(name="panel", description="Legião Panel")
async def panel(interaction: discord.Interaction):
    if interaction.guild and interaction.guild.id == PROTECTED_SERVER_ID:
        await interaction.response.send_message("This command cannot be used inside the protected server.", ephemeral=True)
        return
    try:
        protected_guild = client.get_guild(PROTECTED_SERVER_ID)
        if not protected_guild:
            await interaction.response.send_message("Bot is not in the protected server.", ephemeral=True)
            return
        member = protected_guild.get_member(interaction.user.id)
        if not member:
            member = await protected_guild.fetch_member(interaction.user.id)
        if not member:
            embed = discord.Embed(title="Escolha seu idioma", description="""```
Por favor, selecione seu idioma para continuar.

Please select your language to continue.

Пожалуйста, выберите ваш язык, чтобы продолжить.
```""", color=0x000000)
            await interaction.response.send_message(embed=embed, view=LanguageSelectView(is_access_denied=True), ephemeral=True)
            return
    except:
        embed = discord.Embed(title="Escolha seu idioma", description="""```
POR FAVOR, SELECIONE SEU IDIOMA PARA CONTINUAR.

Este passo é necessário para que o sistema possa configurar corretamente toda a interface, mensagens e funcionalidades de acordo com sua preferência.

Ao selecionar um idioma, todas as comunicações futuras, instruções e respostas serão exibidas automaticamente na linguagem escolhida.

Caso você não selecione um idioma agora, algumas funções podem não ser exibidas corretamente ou podem permanecer no idioma padrão do sistema.

PLEASE SELECT YOUR LANGUAGE TO CONTINUE.

This step is required so the system can properly configure all interface elements, messages, and features according to your preference.

By selecting a language, all future communications, instructions, and responses will be automatically displayed in the chosen language.

If no language is selected now, some features may not display correctly or may remain in the system default language.

ПОЖАЛУЙСТА, ВЫБЕРИТЕ ЯЗЫК ДЛЯ ПРОДОЛЖЕНИЯ.

Этот шаг необходим для правильной настройки интерфейса, сообщений и функций системы в соответствии с вашими предпочтениями.

После выбора языка все будущие сообщения и инструкции будут автоматически отображаться на выбранном языке.

Если язык не будет выбран сейчас, некоторые функции могут отображаться некорректно или оставаться на языке по умолчанию системы.
```""", color=0x000000)
        await interaction.response.send_message(embed=embed, view=LanguageSelectView(is_access_denied=True), ephemeral=True)
        return

    user_lang = get_user_language(interaction.user.id)
    if user_lang is None:
        embed = discord.Embed(title="Escolha seu idioma", description="""```
Por favor, selecione seu idioma para continuar.

Please select your language to continue.

Пожалуйста, выберите ваш язык, чтобы продолжить.
```""", color=0x000000)
        await interaction.response.send_message(embed=embed, view=LanguageSelectView(is_access_denied=False), ephemeral=True)
    else:
        trans = LANGUAGES.get(user_lang, LANGUAGES["pt"])
        embed = discord.Embed(title=trans["title"], description=trans["description"].format(mention=interaction.user.mention), color=0x000000)
        embed.set_author(name="Legião Bot")
        view = LegiaoView(lang=user_lang)
        await interaction.response.send_message(embed=embed, view=view, ephemeral=True)

if __name__ == "__main__":
    client.run(TOKEN)
