import os 
from gtts import gTTS
from time import sleep


class AudioTools:
    def __init__(self,language):
        self.language = language
        

    def find_files(self): 
        filenames =[]
        ls_dir = os.listdir(os.getcwd())
        for x in ls_dir:
            filename, extension = os.path.splitext(x)
            if extension == '.txt':
                print(x)
                filenames.append(x)
        return filenames

    def make_audio(self, filename):
        self.filename = filename

        with open(filename , 'r' ) as rf: 
            data = rf.readlines()
            r_text = ' '.join(data)

            fname , ext = os.path.splitext(filename)
            tts = gTTS(r_text, lang=self.language)
            tts.save(f'{fname}.mp3')
        sleep(1)
        

if __name__ == '__main__':  
    
    language = 'de'
    tools = AudioTools(language)
    text_files = tools.find_files()
    print(text_files)

    for text in text_files: 
        tools.make_audio(text)
