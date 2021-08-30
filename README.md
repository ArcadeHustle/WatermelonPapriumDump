*Reminder, if you like these repos, fork them so they don't disappear*
https://github.com/ArcadeHustle/WatermelonPapriumDump/fork

Big thanks to Fonzie for allowing this to be published.
- written by hostile, with supporting information from the community at large!
<p align="center">
<img src="https://github.com/ArcadeHustle/WatermelonPapriumDump/blob/main/FonzieWMProjectLittleMan.jpg">
</p>

# Project Little Man 
Details on efforts to dump the contents of the Watermelon Games Paprium cart.<br>

[Paprium Press Release 03/16/2017](http://www.paprium.com/press/?language=en)<br>

[![Paprium launch](http://img.youtube.com/vi/f3CTqTzkgZQ/0.jpg)](https://www.youtube.com/watch?v=f3CTqTzkgZQ)<br>

## DATENMEISTER DT128M16VA1LT
The "secret" chip made by [Daten Semiconductor](https://web.archive.org/web/20190706065046/http://datensemi.com/), that is really just a bunch of comodity parts covered in black epoxy glob top encapsulate.<br>

### Main Components as related to potential data storage, or game logic. 
Altera 10M02SCU169C8G FPGA (UBGA169)<br>
https://www.mouser.com/datasheet/2/612/m10_overview-2401081.pdf<br>
https://www.intel.com/content/dam/www/programmable/us/en/pdfs/literature/an/an556.pdf

ST STM32F446ZEJ6 MCU (UFBGA144)<br>
https://www.st.com/resource/en/datasheet/stm32f446re.pdf<br>

Spansion GL064N Series Flash (BGA48)<br>
https://www.cypress.com/file/202426/download<br>

24C64WP EEprom (SO8)<br>
https://www.st.com/resource/en/datasheet/m24c64-f.pdf<br>

### Known Eratta & Useful info for attacking the above components
Several components on the Paprium cart, in particular beneath the black goop on the DT128M16VA1LT are succeptable to known weaknesses, and potential attacks.<br>

#### Intel® MAX 10 FPGAs
https://arxiv.org/abs/1910.05086<br>
https://arxiv.org/pdf/1910.05086.pdf<br>
https://www.youtube.com/watch?v=Ev28MXJdjHE<br>
https://www.cl.cam.ac.uk/~sps32/HWIO_MAX10.pdf<br>
https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-0574<br>
https://www.intel.com/content/www/us/en/security-center/advisory/intel-sa-00349.html<br>

#### STM32F4
https://twitter.com/The_Hpman/status/1383191393393389570<br>
https://twitter.com/The_Hpman/status/1383191380743356416<br>
https://lists.gnupg.org/pipermail/gnuk-users/2020-February/000243.html<br>
https://www.synacktiv.com/sites/default/files/2020-11/presentation.pdf<br>
https://www.st.com/resource/en/application_note/dm00493651-introduction-to-stm32-microcontrollers-security-stmicroelectronics.pdf<br>
https://tches.iacr.org/index.php/TCHES/article/download/7390/6562/<br>
https://blog.kraken.com/post/3662/kraken-identifies-critical-flaw-in-trezor-hardware-wallets/<br>

## Useful tools
https://www.aliexpress.com/item/32820731419.html<br>
https://github.com/atx/python-feeltech<br>
https://www.st.com/en/evaluation-tools/nucleo-f446re.html<br>
https://store.newae.com/stm32f4-target-for-cw308-arm-cortex-m4-1mb-flash-192kb-sram/<br>

### Cart Specific detail

#### Megawire 4.0 (MW4.0)
https://warosu.org/vr/thread/7319474#p7322579<br>

#### Exposed vias on rear of cart
Vias on the cart expose the BGA ball array from the STM32F4, making the epoxy less effective at protecting it. 

## References
https://www.facebook.com/110283612372658/posts/2326873840713613/<br>
https://web.archive.org/web/20190417023031/http://magicalgamefactory.com/en/boards/paprium-about_24/<br>
https://web.archive.org/web/20190226071931/http://www.magicalgamefactory.com/en/blogs/wm-blog_1/<br>
https://papriumfiasco.wordpress.com/tag/datenmeister/<br>
https://github.com/MiSTer-devel/Genesis_MiSTer/issues/158<br>
https://twitter.com/St1ka/status/1364024924873097216<br>
https://twitter.com/MyLifeInGaming/status/1341092115250630656<br>
https://twitter.com/watermelongames/status/1365356392022966278<br>
https://twitter.com/watermelongames/status/1428150734361661440<br>
https://twitter.com/watermelongames/status/1366710552005906439<br>
https://twitter.com/watermelongames/status/1428156649823424512<br>
https://twitter.com/watermelongames/status/1428157032549556225<br>
https://twitter.com/watermelongames/status/1428159286388133892<br>
https://twitter.com/watermelongames/status/1428162198078164997<br>
https://twitter.com/watermelongames/status/1428164359923118086<br>
https://www.youtube.com/watch?v=fukGY5wDTiQ<br>
https://www.youtube.com/watch?v=lxByzNzWTlI<br>
https://www.youtube.com/watch?v=xQTD0Z4tWvE<br>
https://www.youtube.com/watch?v=sFfNuhEyzD0<br>
https://www.youtube.com/watch?v=2it-3NwZ9Go<br>
https://www.youtube.com/watch?v=Nj2LM1rvFQ8<br>
https://www.youtube.com/watch?v=kATTdGY8HkI<br>
https://www.youtube.com/watch?v=bhHp5Q7LUbs<br>
https://www.youtube.com/watch?v=VUaAEqiIi_s<br>
https://www.youtube.com/watch?v=Nj2LM1rvFQ8<br>
https://www.youtube.com/watch?v=svHHCMNOvN8<br>
https://www.youtube.com/watch?v=x482W3m8P7I<br>
https://www.youtube.com/watch?v=BXr229U9430<br>
https://www.youtube.com/watch?v=kXLtnqbeBNI<br>
https://www.youtube.com/watch?v=kOiM7ikcBx0<br>
https://www.youtube.com/watch?v=jbBIua_BXjc<br>
https://www.youtube.com/watch?v=PdUTPv038HE<br>
https://www.change.org/p/paypal-paypal-usa-please-transfer-the-money-to-watermelon-for-releasing-the-game-paprium<br>



