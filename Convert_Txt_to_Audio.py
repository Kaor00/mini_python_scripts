from gtts import gTTS

audio = 'audio.mp3'
language = 'ru'

sp = gTTS(text="Ума, меня попросили передать признание в любви."
               " Я хороший робо голос и с радостью передаю сообщение!",
          lang=language, slow=False)

sp.save(audio)
