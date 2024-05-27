# hamster-kombat-clicker

![hamster kombat](https://i.ibb.co/hXZf0c2/image.png)

## Imkoniyatlar:

- Bosish nuqtalarini orticha harakatlarsiz kalibrovka qilish
- Bosish nuqtasini belgilangan maydonda tasodifiylashtirish
- Mayning qila olish chegarasini avtomatik aniqlash
- Mayning chegarasini simulyatsiya qilish
- Antibotdan himoyat

## O'rnatish:

```bash
chmod +x install.sh
./install.sh
```

## Sozlash:

```
[settings]
x_position = 4488
y_position = 864
interval = 0.1
variation = 60
check_interval = 3
lower_threshold_min = 900
lower_threshold_max = 1100
upper_threshold_min = 1400
upper_threshold_max = 1600
screenshot_region = 4331,1033,97,21
```

| Qiymat |Vazifa|
|--|--|
|`x_position`| Clicker uchun x pozitsiyasi (kalibrator orqali aniqlanadi) |
|`y_position`| Clicker uchun y pozitsiyasi (kalibrator orqali aniqlanadi)|
|`interval`| Click qilish uchun interval|
|`variation`| Clicker qilish maydoni uchun chegara (px da)|
|`check_interval`| Rasmdan aniqlash intervali|
|`lower_threshold_min`| Kichik qiymat uchun minimal mayning diapazoni |
|`lower_threshold_max`| Kichik qiymat uchun maksimal mayning diapazoni |
|`upper_threshold_min`| Katta qiymat uchun minimal mayning diapazoni|
|`upper_threshold_max`| Katta qiymat uchun maksimal mayning diapazoni|
|`screenshot_region`| Rasmdan aniqlash maydoni (kalibrator orqali aniqlanadi)|

## Foydalanish

- [web.telegram.org](https://web.telegram.org) orqali telegramga avtorizatsiya qilinadi
- Google Chrome brauzeriga [Resource Override](https://chromewebstore.google.com/detail/resource-override/pkoacgokdfckfpndoffpifphamojphii) ilovasi o'rnatiladi
- Resource Override ilovasi sozlamalasidan **Tab URL:** qismiga `*`, **from** maydoniga `https://hamsterkombat.io/js/telegram-web-app.js` va **to** maydoniga `https://ktnff.tech/hamsterkombat/telegram-web-app.js` yoziladi
- [web.telegram.org](https://web.telegram.org) orqali o'yin oynasi ochiladi
- `python3 calibrate.py` buyrug'i orqali dastur kalibrovka qilinib `python3 click.py` orqali ishga tushiriladi

## Qo'llab-quvvatlash

Muallifni qo'llab-quvvatlash va donatingni ushbu havola orqali amalga oshirsangiz bo'ladi https://tirikchilik.uz/yetimdasturchi