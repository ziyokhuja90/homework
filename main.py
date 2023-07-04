
# from googletrans import Translator

# translator = Translator()

# translator.translate('안녕하세요.')
# from google_translator_simplified import Translator

# print(Translator.get_translation('pl', 'text for translation', 'en')) #'Tekst do tłumaczenia '
# Translator.get_translation('de', 'tekst do przetłumaczenia', 'pl') #'Text für die Übersetzung '
# Translator.get_translation('pl', 'text for translation') #'Tekst do tłumaczenia '
# Translator.get_translation('de', 'tekst do przetłumaczenia') #'Text für die Übersetzung '



from translate import Translator

while True:
    ask = input('qaysi suzni tarjima qilmoqchisiz>>> ')
    # uz = input('uzbek tiliga tarjima qilmoqchimisiz>>>')
    
    translator= Translator(to_lang="uz")

    translation = translator.translate(ask)

    print(translation)
    
