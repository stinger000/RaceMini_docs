# Сборка гоночного дрона COEX Race Mini

<picture>
   <source srcset="img/avif/drone.avif" type="image/avif">
   <img src="img/drone.jpg" alt="описание" />
</picture>

COEX Race Mini - дрон который предназначен для гонок! При помощи него вы с легкостью освоите спортивное пилотирование.
Тренируйтесь и побеждайте! Увидимся на соревнованиях


## Комплект поставки
Внешний вид коробки:
<picture>
     <source srcset="img/avif/box.avif" type="image/avif">
     <img src="img/box.jpg" alt="описание" />
 </picture>
Содержимое:
<picture>
     <source srcset="img/avif/box_content.avif" type="image/avif">
     <img src="img/box_content.jpg" alt="описание" />
 </picture>

## Установка моторов
Установите ребро жесткости на раму, как это показано на видео:
<video controls width="100%" preload="metadata">
<source src="video/hack.av1.mp4" type="video/mp4">
<source src="video/hack.webm" type="video/webm">
<source src="video/hack.mp4" type="video/mp4">
</video>
Изначально моторы поставляются с проводами одинаковой длины:
<picture>
     <source srcset="img/avif/motor.avif" type="image/avif">
     <img src="img/motor.jpg" alt="описание" />
 </picture>
Два мотора (они будут вращаться по часовой стрелке) обрежьте как показано на рисунке: нижний провод должен быть длиной 60 миллиметров, обозначим его буквой <span style="color:lime">А</span>; средний провод должен быть длиной 65 миллиметров, обозначим его буквой <span style="color:blue">В</span>; верхний провод должен быть длиной 70 миллиметров, обозначим его буквой <span style="color:red">С</span>.
<picture>
     <source srcset="img/avif/motor_cut_cw.avif" type="image/avif">
     <img src="img/motor_cut_cw.jpg" alt="описание" />
 </picture>
Другие два мотора (они будут вращаться против часовой стрелки) обрежьте как показано на другом рисунке:
<picture>
     <source srcset="img/avif/motor_cut_ccw.avif" type="image/avif">
     <img src="img/motor_cut_ccw.jpg" alt="описание" />
 </picture>
Снимите 3 миллиметра изоляции с каждого провода и залудите их. Расположение моторов на дроне будет следующим: моторы, вращающиеся против часовой стрелки находятся на местах 1 и 4, моторы, вращающиеся по часовой стрелке располагаются на местах 2 и 3. На данном рисунке направление переда рамы обозначено стрелкой.
<picture>
     <source srcset="img/avif/motors_tined.avif" type="image/avif">
     <img src="img/motors_tined.jpg" alt="описание" />
 </picture>
Установите моторы на места и закрепите с обратной стороны рамы, используя винты М2 из набора моторов:
<picture>
     <source srcset="img/avif/motors_bolts.avif" type="image/avif">
     <img src="img/motors_bolts.jpg" alt="описание" />
 </picture>
<picture>
     <source srcset="img/avif/motors_mounted.avif" type="image/avif">
     <img src="img/motors_mounted.jpg" alt="описание" />
 </picture>

## Установка ESC
Внешний вид ESC и кабеля питания:
<picture>
     <source srcset="img/avif/esc.avif" type="image/avif">
     <img src="img/esc.jpg" alt="описание" />
 </picture>
Обрежьте кабель питания до длины в 20 миллиметров:
<picture>
     <source srcset="img/avif/esc_cut.avif" type="image/avif">
     <img src="img/esc_cut.jpg" alt="описание" />
 </picture>
Снимите три миллиметра изоляции и залудите провода:
<picture>
     <source srcset="img/avif/esc_tined.avif" type="image/avif">
     <img src="img/esc_tined.jpg" alt="описание" />
 </picture>
 Припаяйте их к плате, соблюдая полярность: красный провод необходимо подключить к контакту, обозначенному знаком +, а черный - к контакту, обозначенному знаком - :
<picture>
     <source srcset="img/avif/esc_soldered.avif" type="image/avif">
     <img src="img/esc_soldered.jpg" alt="описание" />
 </picture>
Установите силиконовые проставки в отверстия:
<picture>
     <source srcset="img/avif/esc_orings.avif" type="image/avif">
     <img src="img/esc_orings.jpg" alt="описание" />
 </picture>
Более длинная часть должна быть направлена вверх:
<picture>
     <source srcset="img/avif/esc_orings_pos.avif" type="image/avif">
     <img src="img/esc_orings_pos.jpg" alt="описание" />
 </picture>
Вставьте шлейф в плату регуляторов:
<picture>
     <source srcset="img/avif/esc_cable.avif" type="image/avif">
     <img src="img/esc_cable.jpg" alt="описание" />
 </picture>
Установите плату регуляторов со шлейфом в корпус, закрутите винтами М2x20 с обратной стороны.
<picture>
     <source srcset="img/avif/esc_placed.avif" type="image/avif">
     <img src="img/esc_placed.jpg" alt="описание" />
 </picture>
Припаяйте выводы моторов к контактным площадкам: на рисунке ниже буква
 <span style="color:lime">А</span>
 соответствует короткому проводу, буква
 <span style="color:blue">В</span> -
 среднему, а буква
 <span style="color:red">С</span> -
 длинному проводу.
<picture>
     <source srcset="img/avif/esc_motors.avif" type="image/avif">
     <img src="img/esc_motors.jpg" alt="описание" />
 </picture>
Вид сбоку:
<picture>
     <source srcset="img/avif/esc_side.avif" type="image/avif">
     <img src="img/esc_side.jpg" alt="описание" />
 </picture>

## Установка полетного контроллера

Внешний вид полетного контроллера:
<picture>
     <source srcset="img/avif/fc.avif" type="image/avif">
     <img src="img/fc.jpg" alt="описание" />
 </picture>

### Подключение видеопередатчика
Видеопередатчик находится внутри этой коробочки:
<picture>
     <source srcset="img/avif/vtx_pack.avif" type="image/avif">
     <img src="img/vtx_pack.jpg" alt="описание" />
 </picture>
Внутри находится сам видеопередатчик, адаптер для установки в отверстия 20х20 (он нам не понадобится), антенна, переходник для установки другой антенны (он также не понадобится) и провода:
<picture>
     <source srcset="img/avif/vtx_pack_content.avif" type="image/avif">
     <img src="img/vtx_pack_content.jpg" alt="описание" />
 </picture>
На верхней стороне видеопередатчика находятся подписи контактных площадок:
<picture>
     <source srcset="img/avif/vtx_top.avif" type="image/avif">
     <img src="img/vtx_top.jpg" alt="описание" />
 </picture>
С другой стороны располагается разъем для антенны и кнопка переключения каналов:
<picture>
     <source srcset="img/avif/vtx_bottom.avif" type="image/avif">
     <img src="img/vtx_bottom.jpg" alt="описание" />
 </picture>
Припаяйте провода к видеопередатчику в следующей последовательности:
<span style="color:red">красный</span>
провод к контакту +5V, **черный** - к контакту GND,
<span style="color:goldenrod;">желтый</span> - к контакту VIDEO и
<span class="outlined">белый</span> - к контакту RX:
<picture>
     <source srcset="img/avif/vtx_cable.avif" type="image/avif">
     <img src="img/vtx_cable.jpg" alt="описание" />
 </picture>
Вставите антенну в видеопередатчик:
<picture>
     <source srcset="img/avif/vtx_antenna.avif" type="image/avif">
     <img src="img/vtx_antenna.jpg" alt="описание" />
 </picture>
Наденьте термоусадку на видеопередатчик и усадите её потоком горячего воздуха:
<picture>
     <source srcset="img/avif/vtx_heatshrink.avif" type="image/avif">
     <img src="img/vtx_heatshrink.jpg" alt="описание" />
 </picture>
Обрежьте провода до длины в 60 миллиметров, залудите на 3 миллиметра и припаяйте провода к полетному контроллеру в следующей последовательности:
<span style="color:red">красный</span>
провод к контакту +5V, **черный** - к контакту G,
<span style="color:goldenrod;">желтый</span> - к контакту VO и
<span class="outlined">белый</span> - к контакту T1:
<picture>
     <source srcset="img/avif/vtx_pads.avif" type="image/avif">
     <img src="img/vtx_pads.jpg" alt="описание" />
 </picture>
Вот так это будет выглядеть:
<picture>
     <source srcset="img/avif/vtx_soldered.avif" type="image/avif">
     <img src="img/vtx_soldered.jpg" alt="описание" />
 </picture>


### Подключение камеры


Внешний вид камеры:
<picture>
     <source srcset="img/avif/cam.avif" type="image/avif">
     <img src="img/cam.jpg" alt="описание" />
 </picture>
Обрежьте ответный кабель разъема камеры на длину в 50 миллиметров, и залудите концы на длину в 3 миллиметра. Припаяйте его к полетному контроллеру в следующем порядке:
**черный** провод - к контакту G,
<span style="color:goldenrod;">желтый</span> - к контакту VI,
<span style="color:red">красный</span> - к контакту +5 вольт, как показано на схеме:
<picture>
     <source srcset="img/avif/cam_pads.avif" type="image/avif">
     <img src="img/cam_pads.jpg" alt="описание" />
 </picture>
Припаянный провод должен выглядеть следующим образом:
<picture>
     <source srcset="img/avif/cam_cable_soldered.avif" type="image/avif">
     <img src="img/cam_cable_soldered.jpg" alt="описание" />
 </picture>

### Подключение светодиодной ленты

В комплекте со светодиодной лентой идет провод:
<picture>
     <source srcset="img/avif/led_cable.avif" type="image/avif">
     <img src="img/led_cable.jpg" alt="описание" />
 </picture>
Припаяйте провода к полетному контроллеру в следующей последовательности:
**G** к контакту G,
<span style="color:red">5v</span> к контакту B+ полетного контроллера, и
<span style="color:goldenrod;">sig</span> к контакту LED, как показано на схеме:
<picture>
     <source srcset="img/avif/led_pads.avif" type="image/avif">
     <img src="img/led_pads.jpg" alt="описание" />
 </picture>
Припаянный провод должен выглядеть следующим образом:
<picture>
     <source srcset="img/avif/led_soldered.avif" type="image/avif">
     <img src="img/led_soldered.jpg" alt="описание" />
 </picture>

### Подключение радиоприемника

Внешний вид радиоприемника:
<picture>
     <source srcset="img/avif/rc.avif" type="image/avif">
     <img src="img/rc.jpg" alt="описание" />
 </picture>
Обрежьте провода приемника на длину 50 миллиметров и залудите концы на длину 3 миллиметра. Припаяйте провода к полетному контроллеру в следующем порядке:
<span style="color:red">красный</span>
провод к контакту +5V, **черный** - к контакту G,
<span style="color:goldenrod;">желтый</span> - к контакту R2, как показано на рисунке:
<picture>
     <source srcset="img/avif/rc_pads.avif" type="image/avif">
     <img src="img/rc_pads.jpg" alt="описание" />
 </picture>
Припаянный провод должен выглядеть следующим образом:
<picture>
     <source srcset="img/avif/rc_cable.avif" type="image/avif">
     <img src="img/rc_cable.jpg" alt="описание" />
 </picture>
Наденьте термоусадку на радиоприемник и усадите:
<picture>
     <source srcset="img/avif/rc_shrinked.avif" type="image/avif">
     <img src="img/rc_shrinked.jpg" alt="описание" />
 </picture>
После этого подключите приемник к припаянному только что кабелю.

### Установка полетного контроллера в корпус
Вставьте силиконовые проставки в полетный контроллер в соответствие со схемой:
<picture>
     <source srcset="img/avif/fc_orings_pos.avif" type="image/avif">
     <img src="img/fc_orings_pos.jpg" alt="описание" />
 </picture>
Подключите шлейф, идущий от регуляторов к полетному контроллеру, установите его в корпус и зафиксируйте гайками:
<picture>
     <source srcset="img/avif/fc_nuts.avif" type="image/avif">
     <img src="img/fc_nuts.jpg" alt="описание" />
 </picture>
<picture>
     <source srcset="img/avif/fc_placed.avif" type="image/avif">
     <img src="img/fc_placed.jpg" alt="описание" />
 </picture>

## Подключение аппаратуры радиоуправления

Если сейчас подключить аккумулятор к дрону, то светодиод на приемнике начнет медленно мигать:
<picture>
   <source srcset="img/rx_unbinded.avif" type="image/avif">
   <source srcset="img/rx_unbinded.webp" type="image/webp">
   <img src="img/rx_unbinded.gif" alt="описание" />
</picture>
Это означает, что радиоприемник не получает сигнал от аппаратуры радиоуправления. Такое может происходить в двух случаях:

1. Аппаратура радиоуправления выключена
2. Радиоприемник и аппаратура радиоуправления не настроены для работы друг с другом

Для радиоуправления дроном необходимо настроить радиоприемник на работу с конкретной радиоаппаратурой (данная процедура называется bind). Для этого необходимо при выключенном питании дрона нажать кнопку Bind на радиоприемнике, после чего с зажатой кнопкой подключить аккумулятор. Светодиод на радиоприемнике начнет быстро мигать:
<img src="img/rx_binding.gif" width="100%"
  height="100" alt="Иллюстрация">

После этого зажмите кнопку Bind на аппаратуре управления и включите ее:
<picture>
     <source srcset="img/avif/app_off.avif" type="image/avif">
     <img src="img/app_off.jpg" alt="описание" />
 </picture>
В случает успеха светодиод на радиоприемнике будет гореть постоянно:
<picture>
     <source srcset="img/avif/rc_binded.avif" type="image/avif">
     <img src="img/rc_binded.jpg" alt="описание" />
 </picture>
А на экране аппаратуры радиоуправления будет отображаться напряжение питания приемника:
<picture>
     <source srcset="img/avif/app_binded.avif" type="image/avif">
     <img src="img/app_binded.jpg" alt="описание" />
 </picture>
## Финальная сборка

Внешний вид канопы с камерой:
<picture>
     <source srcset="img/avif/final_canopy.avif" type="image/avif">
     <img src="img/final_canopy.jpg" alt="описание" />
 </picture>
Установите камеру внутри канопы и зафиксируйте винтами:
<picture>
     <source srcset="img/avif/final_cam_mounted.avif" type="image/avif">
     <img src="img/final_cam_mounted.jpg" alt="описание" />
 </picture>
Подключите камеру к полетному контроллеру. Расположите радиоприемник и видеопередатчик внутри канопы. Проденьте разъемы для светодиодных лент в отверстия канопы и подключите их.
<picture>
     <source srcset="img/avif/final_led.avif" type="image/avif">
     <img src="img/final_led.jpg" alt="описание" />
 </picture>
Защелкните светодиодные ленты в их посадочных местах:
<picture>
     <source srcset="img/avif/final_led_mounted.avif" type="image/avif">
     <img src="img/final_led_mounted.jpg" alt="описание" />
 </picture>
Подключите переходник USB и выполните
[настройку дрона](setup):
<picture>
     <source srcset="img/avif/final_usb.avif" type="image/avif">
     <img src="img/final_usb.jpg" alt="описание" />
 </picture>
После того, как настройка закончена, защелкните канопу на дроне:
<picture>
     <source srcset="img/avif/final_canopy_locked.avif" type="image/avif">
     <img src="img/final_canopy_locked.jpg" alt="описание" />
 </picture>
Переверните дрон нижней стороной вверх:
<picture>
     <source srcset="img/avif/final_bottom.avif" type="image/avif">
     <img src="img/final_bottom.jpg" alt="описание" />
 </picture>
Наклейте противоскользящую накладку:
<picture>
     <source srcset="img/avif/final_silicon.avif" type="image/avif">
     <img src="img/final_silicon.jpg" alt="описание" />
 </picture>
На этом сборка завершена.
