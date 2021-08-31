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
The "custom" chip made by [Daten Semiconductor](https://web.archive.org/web/20190706065046/http://datensemi.com/), that is really just a bunch of comodity parts covered in black [epoxy glob top encapsulant](https://www.youtube.com/watch?v=dRsl4c6NM8U). Never mind that ["Datenmeister DT128M16VA1LT chipset is fake"](https://papriumfiasco.wordpress.com/tag/datenmeister/), or that the website of the company that "makes" it, was originally registered to Fonzie. 

### Main Components as related to potential data storage, or game logic. 
Several components of "DT128M16VA1LT" on the Paprium cart are succeptable to known weaknesses, and potential attacks. Being beneath black goop does not at all make the chips impervious to attack.<br>

#### Intel® MAX 10 FPGAs
Altera 10M02SCU169C8G FPGA (UBGA169)<br>
https://www.mouser.com/datasheet/2/612/m10_overview-2401081.pdf<br>
https://www.intel.com/content/dam/www/programmable/us/en/pdfs/literature/an/an556.pdf

The Intel FPGA on the Paprium cart ["may allow an authenticated user to potentially enable escalation of privilege and information disclosure via physical access"](https://www.intel.com/content/www/us/en/security-center/advisory/intel-sa-00349.html). The vulnerability has been assigned [CVE-2020-0574](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-0574). Dr. Sergei Skorobogatov of the Dept of Computer Science and Technology, University of Cambridge, Cambridge, UK, has been credited with reporting this issue. His papers and persentations on the subject are linked below:<br> 
https://arxiv.org/abs/1910.05086<br>
https://arxiv.org/pdf/1910.05086.pdf<br>
https://www.cl.cam.ac.uk/~sps32/HWIO_MAX10.pdf<br>

[![Hardware security evaluation of Intel MAX 10 FPGAs | Dr. Sergei Skorobogatov](http://img.youtube.com/vi/Ev28MXJdjHE/0.jpg)](https://www.youtube.com/watch?v=Ev28MXJdjHE)<br>

#### STM32F4
ST STM32F446ZEJ6 MCU (UFBGA144)<br>
https://www.st.com/resource/en/datasheet/stm32f446re.pdf<br>
https://www.st.com/resource/en/application_note/dm00493651-introduction-to-stm32-microcontrollers-security-stmicroelectronics.pdf<br>

STM32F4 is known vulnerable to voltage glitching attacks. The attacks have moved from theory, and manual one off demonstrations to now being available in ready made productized form with tools like [ChipWhisperer](https://www.newae.com/chipwhisperer)<br>.
Various demonstrations have occured outside lab constraints, with SDK kits. Real, actual products have been attacked at this point. The exploitation techniques are reliable:<br> 
https://lists.gnupg.org/pipermail/gnuk-users/2020-February/000243.html<br>
https://www.synacktiv.com/sites/default/files/2020-11/presentation.pdf<br>
https://tches.iacr.org/index.php/TCHES/article/download/7390/6562/<br>
https://blog.kraken.com/post/3662/kraken-identifies-critical-flaw-in-trezor-hardware-wallets/<br>

[TheHpman](https://wiki.mamedev.org/index.php/TheHpman) appears to have done some basic reversing of the cart, but did not fully disclose which components he worked with. The logic used by the STM32 is explictly mentioned on his Twitter account:<br>
https://twitter.com/The_Hpman/status/1383191393393389570<br>
https://twitter.com/The_Hpman/status/1383191380743356416<br>

[BreakIC](http://www.break-ic.com) aka Mikatech will dump the STM32 for a fee of $6500 USD, claiming that "The tools needed to read it costs USD2million". Mikatech claims to be "World first mcu cloning company", we have reliably used them in the past for less costly extractions. Worst case scenario, we could pay to have the chip dumped via this method, albiet costly<br>
<img src="https://github.com/ArcadeHustle/WatermelonPapriumDump/blob/main/breakIC.jpg">

Practicing on [STM32F4 dev boards](https://www.st.com/en/evaluation-tools/nucleo-f446re.html) using a standard ChipWhisperer setup should set the stage for dumping the Paprium STM32F4. <br>

Similarly starting with the standard [STM43F4 "UFO" target board](https://store.newae.com/stm32f4-target-for-cw308-arm-cortex-m4-1mb-flash-192kb-sram) is a great way to practice before moving on to attack the Paprium cart.<br>

### MirrorBit Flash
Spansion GL064N Series Flash (BGA48)<br>
https://www.cypress.com/file/202426/download<br>

Reading the Spansion flash should be possible with a standard Universal Programmer, and the appropriate adapter. 
https://www.aliexpress.com/item/32820731419.html<br>
https://www.aliexpress.com/item/32978614065.html<br>

### i2c EEPROM
24C64WP EEprom (SO8)<br>
https://www.st.com/resource/en/datasheet/m24c64-f.pdf<br>

Similarly reading the i2c EEPROM should be possible with standard EEPROM readers, or even an [Arduino](https://learn.sparkfun.com/tutorials/reading-and-writing-serial-eeproms/all). 

## Useful tools
The standard tool for voltage glitching is the Chip Whisperer, STM32 is a default target in the "level 1" kit, so this seems like a natural fit for anyone wanting to play along:<br>
https://store.newae.com/side-channel-glitching-starter-pack-level-1/<br>
https://www.mouser.com/new/newae-technology/newae-chipwhisperer-lite-l1-kit/<br>

Before the ChipWisperer came along you often saw [FeelTech FY3200S](https://www.ebay.com/itm/402781810775) used in academic papers about voltage glitching STM32. This device contains a USB API that can be used to script voltage changes.<br>
https://github.com/atx/python-feeltech<br>

### Cart Specific detail
The Paprium cart is a special unicorn. If you don't pay attention, you may perhaps miss some notable "features".<br>

#### Megawire 4.0 (MW4.0)
Described in the manual as being used to "Connect to PAPRIUM's NXT network and enable the game's online services.". It can also be used because "Some game updates may be available for download. Nobody's perfect...", or for DLC that "can be purchased with GEMS".<br>

"Megawire 4.0 is a special connector that has 4 segments to it. There are 2 segments for data transfer & 2 for are for power & ground."
https://warosu.org/vr/thread/7319474<br>

#### Exposed vias on rear of cart
Vias on the cart expose the BGA ball array from the STM32F4, making the epoxy less effective at protecting it. 
<img src="https://github.com/ArcadeHustle/WatermelonPapriumDump/blob/main/exposedVIAs.jpg">

## References
These are random related backstory items that make for good reading, or listening.<br>

https://www.facebook.com/110283612372658/posts/2326873840713613/<br>
https://web.archive.org/web/20190417023031/http://magicalgamefactory.com/en/boards/paprium-about_24/<br>
https://web.archive.org/web/20190226071931/http://www.magicalgamefactory.com/en/blogs/wm-blog_1/<br>
https://papriumfiasco.wordpress.com/tag/datenmeister/<br>
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
