# Pronounce me like one of your French numbers
Analysis on the duration of pronunciation of numbers.
**This is a useless project !**

**Caution :**
* This is a "1 hour project" (nothing is really deeply thinked)
* Number of syllables is calculated with an "english based" library
* Points in graphics are not continuous, but with a fixed increment (see plot titles)

### Results

| length | syllables |
|:------:|:---------:|
| ![length_10000](https://github.com/user-attachments/assets/4bd5b976-14a4-4bf4-96fd-3db130189192)       | ![syllables_10000](https://github.com/user-attachments/assets/a427e3d3-50d2-47f7-aa0e-482d430944f7) |
| ![length_100000](https://github.com/user-attachments/assets/3d824df6-0691-43e6-aa41-0107f3af8b14)      | ![syllables_100000](https://github.com/user-attachments/assets/f84d7569-f12f-45e8-838d-2f2760518f66) |
| ![length_1000000](https://github.com/user-attachments/assets/b6eb5051-534e-4c2e-933c-fc56c3ef5af4)     | ![syllables_1000000](https://github.com/user-attachments/assets/9ac4ee8c-98e2-4653-9a60-6d48c4efdcb5) |
| ![length_10000000](https://github.com/user-attachments/assets/5419a879-e28d-4097-bfb8-15abbe37bc32)    | ![syllables_10000000](https://github.com/user-attachments/assets/6fd02669-4f53-4187-a626-2cab5ef5cc90) |
| ![length_100000000](https://github.com/user-attachments/assets/e6913ee2-3256-4f72-b740-38cebf44a39e)   | ![syllables_100000000](https://github.com/user-attachments/assets/f0ebdfaa-0d05-4bd6-bbcd-7805ae401d31) |
| ![length_1000000000](https://github.com/user-attachments/assets/954029f1-411e-412f-b74e-962288e2a960)  | ![syllables_1000000000](https://github.com/user-attachments/assets/514f152a-7fbb-408c-a704-03473a590ad8) |
| ![length_10000000000](https://github.com/user-attachments/assets/715e7931-149d-42b1-b943-93bb3ac635ff) | ![syllables_10000000000](https://github.com/user-attachments/assets/93d8fabc-be54-43a1-811f-3259ed07086f) |


### Usage

* Install requirements
  * `pip install matplotlib numpy`
  * `pip install num2words`
  * `pip install syllables`
* Run app to generate same results
  * `python main.py`


### Acknowledgement

#### Where did this idea come from ?

I just watched (5 min ago as writing this) a video where the time of pronunciation some big numbers is used as a joke and just thinked : "Can I make stats and plot about this ? Of course I can !"

Source video :  
[![IMAGE ALT TEXT HERE](https://img.youtube.com/vi/EBan7vf37_I/0.jpg)](https://youtu.be/EBan7vf37_I?t=127)

