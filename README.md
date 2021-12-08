# alexa_rpi
Voice controlled home automation system using Amazon Alexa and Raspberry Pi

[![IMAGE ALT TEXT](https://kogyikaunghtet.github.io/assets/img/alexa/alexa.png)](https://www.youtube.com/watch?v=sHf-R44n804 "Alexa_RPi")

<div class="responsive-embed flex-video">
<iframe width="640" height="360" src="https://www.youtube.com/embed/sHf-R44n804" title="YouTube video player" gesture="media" allow="encrypted-media" allowfullscreen></iframe>
</div>

IoT device တွေအနေနဲ့ နာမည်ကြီးတဲ့ Amazon Alexa Echo dot လို voice controlled smart speaker တွေကို Raspberry Pi နဲ့ တွဲဖက် အသုံးပြုမယ်ဆိုရင် Amazon Smart Plug လို ပစ္စည်းတွေ ထပ်သုံးစရာ မလိုတော့ပဲ modify များစွာ ဆက်လုပ်လို့ ရပါတယ်။ ဒီလို Alexa Echo နဲ့ Raspberry Pi ချိတ်ဆက်ပြီး မီး အဖွင့်အပိတ်တွေ ပြုလုပ်ဖို့အတွက် အောက်ပါအတိုင်း program ကို download ရယူပြီး စမ်းသပ်ကြည့်နိုင်ပါတယ်။

`$ git clone https://github.com/kogyikaunghtet/alexa_rpi`
<br>
`$ cd alexa_rpi`

alexa_pi directory အောက်က alexa.py ကို ဖွင့်ဖတ်ကြည့်ရင် yellow, green, red, blue မီးတွေအတွက် Raspberry Pi Physical Pin နံပါတ် 11, 12, 13, 14 ကို အသုံးပြုထားပါတယ်။ alexa.py ကို run ထားပြီး Alexa echo dot ကို <b>“Alexa, discover all devices” </b>လို့ ပြောကာ Raspberry Pi သို့ ချိတ်ဆက်စေနိုင်ပါတယ်။

Raspberry Pi နဲ့ Alexa Echo ချိတ်ဆက်ပြီးနောက် “turn on yellow light” ဖြစ်စေ၊ “turn off yellow light” ဖြစ်စေ voice command ပေးကာ မီးအဖွင့်အပိတ် ပြုလုပ်နိုင်တဲ့အပြင် Alexa App ကနေလည်း အင်တာနက်ရရှိတဲ့ မည်သည့် နေရာမှမဆို On/Off ခလုတ်တွေ နှိပ်ခြင်း၊ Voice command ပေးခြင်းဖြင့် ထိန်းချုပ်ခိုင်းစေနိုင်ပါတယ်။

