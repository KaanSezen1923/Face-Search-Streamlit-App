Güncellenmiş `README.md` dosyanız aşağıdaki gibi olacaktır. Bu dosya, projeniz hakkında genel bir bakış, kurulum talimatları, proje yapısı ve kullanım bilgilerini içerir.

---

# Face Searching Project

Bu proje, kullanıcıların bir görüntü yüklemesine ve önceden kodlanmış bir veri setinden eşleşen yüzleri aramasına olanak tanıyan bir yüz tanıma uygulamasıdır. Uygulama, kullanıcı arayüzü için Streamlit, görüntü işleme için OpenCV ve yüz tespiti ve kodlama için face_recognition kütüphanesini kullanır.

## Özellikler
- Bir görüntü yükleyin ve önceden kodlanmış bir veri setinden eşleşen yüzleri bulun.
- Yüklenen görüntü ve eşleşen sonuçları yan yana gösterin.
- Eşleşme güven seviyesi hakkında geri bildirim sağlayın.

## Kurulum

### Depoyu Klonlayın:
```bash
git clone https://github.com/KaanSezen1923/Face-Search-Streamlit-App.git
cd Face-Search-Streamlit-App
```

### Bir sanal ortam oluşturun ve etkinleştirin:
```bash
python -m venv venv
source venv/bin/activate  # Windows'da `venv\Scripts\activate` kullanın
```

### Gerekli paketleri yükleyin:
```bash
pip install -r requirements.txt
```

## Veri Hazırlığı
Kodlanacak yüzlerin bulunduğu görüntüleri, örneğin `Data` klasörüne yerleştirin.

Kodlanmış verileri oluşturmak için kodlama scriptini çalıştırın:
```bash
python encode_faces.py
```

## Uygulamayı Çalıştırma
Streamlit uygulamasını başlatın:
```bash
streamlit run main.py
```

Uygulamayı kullanmak için sağlanan yerel URL'yi web tarayıcınızda açın.

## Proje Yapısı
```bash
face-searching-project/
│
├── encode_faces.py         # Veri setinden yüzleri kodlamak için script
├── main.py                 # Streamlit uygulama scripti
├── EncodeFile.p            # Kodlanmış veri dosyası
├── requirements.txt        # Gerekli Python paketleri
└── README.md               # Proje dökümantasyonu
└── Data                    # Kodlanacak yüzlerin bulunduğu klasör
```

## Scriptler

### encode_faces.py
Bu script, belirtilen klasörden görüntüleri okur, yüzleri kodlar ve kodlamaları bir dosyaya kaydeder.

### main.py
Bu script, kullanıcıların bir görüntü yüklemesine ve eşleşen yüzleri bulmasına olanak tanıyan Streamlit uygulamasını içerir.

## Gereksinimler
- Python 3.x
- face_recognition
- numpy
- opencv-python
- Pillow
- streamlit
- cmake
- dlib

Tüm bağımlılıkların yüklendiğinden emin olmak için şunu çalıştırın:
```bash
pip install -r requirements.txt
```

## Katkıda Bulunma
İyileştirmeler ve hata düzeltmeleri için sorunlar açmaktan veya pull request göndermekten çekinmeyin.

## Lisans
Bu proje MIT Lisansı altında lisanslanmıştır.

---

Bu içerikle `README.md` dosyanızı güncelleyebilir ve GitHub deposuna ekleyebilirsiniz. Bu talimatlar, projenizi nasıl kullanacağınızı ve kurulum yapacağınızı açıkça belirtir.

![image](https://github.com/KaanSezen1923/Face-Search-Streamlit-App/assets/119515258/36634328-544f-4afe-896b-d03c4a1efcc0)

![image](https://github.com/KaanSezen1923/Face-Search-Streamlit-App/assets/119515258/e647ba8d-b372-464d-aaf8-6f72c7ce92f3)


