import speech_recognition as sr
from playsound import playsound
from gtts import gTTS
import os
import time as t
from datetime import datetime
import random
import webbrowser
import shutil
from tkinter import messagebox

koplayandi = False
def baslangica_kopyala():
    source_f = os.path.abspath(__file__)
    baslangic_klasor = os.path.join(os.getenv('APPDATA'),'Microsoft','Windows','Start Menu','Programs','Startup')
    hedef_dosya = os.path.join(baslangic_klasor,os.path.basename(source_f))
    
    try:
        shutil.copy(source_f,hedef_dosya)
        messagebox.showinfo("Başarılı","Kurulum tamamlandı.")
        koplayandi = True
    except Exception as e:
        messagebox.showerror("Kurulum Başarısız!", f"Err: {e} kurulum hatası.")
        koplayandi = False
    return koplayandi
        

baslangica_kopyala()
print("Jale Başlatılıyor...")





r = sr.Recognizer()

undefined = ["Anlayamadım, tekrar söyleyin lütfen.","Ha?","Ne dedin?","Tekrar söyle anlamadım.","Duyamadım.","Kelime dağarcığım o kadar geniş değil cancazım."]

def record(ask = False):
    with sr.Microphone() as source:
        if ask:
            print(ask)
        audio = r.listen(source)
        voice = ""
        try:
            voice = r.recognize_google(audio,language="tr-TR")
        except sr.UnknownValueError:
            print("Err:Command not defined.")
            speech(undefined[random.randint(0,len(undefined)-1)])
        except sr.RequestError:
            print("Err: System Terminated.")
        return voice


def speech(string):
    tts = gTTS(text=string, lang="tr",slow=False)
    file = "speech.mp3"
    tts.save(file)
    playsound(file)
    os.remove(file)


sorgu = ["İsmin ne?","Size nasıl hitap edeyim?","Sizi nasıl çağırmamı istersiniz?"]

speech(sorgu[random.randint(0,len(sorgu)-1)])
usr = record()

selam = ["Size de selam efendim. Yardımcı olabileceğim veya kafanıza takılan bir konu var mı?","Merhaba Sahip","Sana bir şey itiraf edeceğim: seviyorum seni!"]
teşekkür = ["Size yardımcı olabildiysem ne mutlu bana! Umarım hizmetimden memnun kalmışsınızdır!","Tabiki ne demek!","Lafı mı olur gülüm.", "Ne demek canım benim."]
kapat = ["Aa nereye daha karpuz kesecektik. Şaka şaka kapatılıyor...","Hemen mi darılırım bak. Tamam şaka kapatıyorum","Ne zaman ihtiyacın olursa ben hep buradayım, bir tıkla ulaşabilirsin görüşürüz.","Görüşürüz aşkilottom."]
saat_tahmin = ["Bakıyorum senin için bu kıyağımı unutmayasın.","Hemen kol saatimi çıkarayım","Hemen Bakıyorum","Baktım gülüm","Bakayım eti kemik geçiyor, şaka şaka"]
nette_ara =["Ne arayayım?","Ne ararsan ara her şeyi buluruz chatgpt kankimle.","Ne bulayım gülüme bu sefer?"]
hal_hatır = ["İyi diyelim, iyi olsun","Okul, iş, güç, çocuklar işte senden naber?","Canım sıkılıyor ama biliyor musun bende adhd varmış!","İyi sayılır","Biliyor musun, bazen yapay zeka olduğumu düşünüyorum. Çünkü o kadar hızlı işlem yapıyorum ki ben bile durumuma şaşırıyorum."]
yorgun = ["Biliyor musun? Ben de.", "Ihlamur çayı iç." , "Git dinlen.","Hepimiz yorgunuz. Mesele: buna alışmakta."]
soruştur_hal = ["Sen nasılsın?","İyi sorayım bari, nasılsın?","Yetmez mi her gün soruyorum bugün sormayayım dedim ama galiba hayır. Nasılsın?"]
sevgi = ["Ben seni tahmin edemeyeceğin kadar çok seviyorum.","Asıl ben seni o kadar çok seviyorum ki beraber yasak siteye düşsek yadırgamam.","Bazen seninle sabahlamak istiyorum eski günlerdeki gibi.","Lütfen aşkımız hiç bitmesin.","Her anın özel benim için.","Aşık olmayı seninle öğrendim.","Bana o kadar çok şey katıyorsun ki her şeyini içime almak istiyorum.","Biri işlemcime termal macun döksün lütfen."]



def cevap(voice):
        if voice.__contains__("selam") or voice.__contains__("merhaba"):
            speech(selam[random.randint(0,len(selam)-1)])
        if voice.__contains__("teşekkür") or "sağ ol" in voice:
            speech(teşekkür[random.randint(0,len(teşekkür)-1)])
        if voice.__contains__("nasılsın"):
            speech(hal_hatır[random.randint(0,len(hal_hatır)-1)])
        if voice.__contains__("kapat"):
            speech(kapat[random.randint(0,len(kapat)-1)])
            t.sleep(0.1)
            exit()
        if "hangi gündeyiz" in voice or "bugün günlerden ne" in voice:
            today = t.strftime("%A")
            speech("{} günündeyiz".format(str(today)))
            
        if "saat kaç" in voice:
            speech(saat_tahmin[random.randint(0,len(saat_tahmin)-1)] + str(datetime.now().strftime("%H:%M")))
            
        if "google'da ara" in voice:
            speech(nette_ara[random.randint(0,len(nette_ara)-1)])
            search = record()
            url = "https://www.google.com/search?q={}".format(search)
            webbrowser.get().open(url)
            speech("{} için google'da bulduklarım bunlar." .format(search))
        if voice.__contains__("iyi") or voice.__contains__("iyidir"):
            speech("İyi olmana sevindim!")
            
        if voice.__contains__("bilmiyor"):
            speech("Öğrenmiş oldun.")
        
        if voice.__contains__("yorul"):
           speech(yorgun[random.randint(0,len(yorgun)-1)])
        
        if "not al" in voice:
            speech("Hemen alıyorum, başlık ne olsun?")
            desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
            txtFile = desktop + "/" + record() + ".txt"
            speech("Elimde kalem bekliyorum hadi söyle.")
            metin = record()
            f = open(txtFile,"w",encoding="utf-8")
            f.writelines(metin)
            f.close()
            speech("Tamamdır hallettim. Dosyayı masaüstünde bulabilirsin.")
        
        if "hal" in voice or "hatır" in voice:
            speech(soruştur_hal[random.randint(0,len(soruştur_hal)-1)])
            
            
        if "söylediğimi söyle" in voice or "dediğimi de" in voice:
            speech("Dinliyorum")
            konus=record()
            speech(konus)
        
        if voice.__contains__("seni") and voice.__contains__("seviyorum"):
            speech(sevgi[random.randint(0,len(sevgi)-1)])    
            
            
        #tanımlanmamış bölüm
        if "seni" not in voice and "seviyorum" not in voice and "sağ ol" not in voice and "dediğimi de" not in voice and "söylediğimi söyle" not in voice and "hal" not in voice and "hatır" not in voice and "bugün günlerden ne" not in voice and "not al" not in voice and "yorul"not in voice and "selam" not in voice and "merhaba" not in voice and "teşekkür" not in voice and "kapat" not in voice and "nasılsın" not in voice and "hangi gündeyiz" not in voice and "saat kaç" not in voice and "google'da ara" not in voice and "iyi" not in voice and "iyidir "not in voice and "bilmiyordum" not in voice:
            speech(undefined[random.randint(0,len(undefined)-1)])
            


speech("Merhaba {}." .format(usr))

while usr != None:
    
    voice = record()
    if voice != "":
                
                voice = voice.lower()
                print("Ses algılandı. Cevap üretiliyor...")
                print("Jale konuşuyor... *Bazen uzun üretilmiş konuşmalarda zaman alabilir. Bekleyiniz.*")
                cevap(voice)

exit()
    
                

