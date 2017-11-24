
import os
import distutils.dir_util
import shutil


distutils.dir_util.mkpath('/home/pi/RetroPie/roms/moonlight')


print("Configuring Moonlight as system")
if 'Moonlight' in open('/etc/emulationstation/es_systems.cfg').read():
    print("    Moonlight system exists")
else:
    print("    Adding system!")
    with open('/etc/emulationstation/es_systems.cfg', 'a') as moon_cfg:
        moon_cfg.write("  <system>\n")
        moon_cfg.write("    <name>Moonlight</name>\n")
        moon_cfg.write("    <path>/home/pi/RetroPie/roms/moonlight/</path>\n")
        moon_cfg.write("    <extension>.sh</extension>\n")
        moon_cfg.write("    <command>%ROM%</command>\n")
        moon_cfg.write("    <theme>moonlight</theme>\n")
        moon_cfg.write("  </system>\n")

distutils.dir_util.mkpath('/etc/emulationstation/themes/carbon/moonlight')
distutils.dir_util.mkpath('/etc/emulationstation/themes/carbon/moonlight/art')

# check that ./themes folder exists
print(os.path.isdir("./themes")) # NOTE: Check that relative path works

# cp ./themes/carbon/moonlight/theme.xml to /etc/emulationstation/themes/carbon/moonlight
shutil.copy2("./themes/carbon/moonlight/theme.xml", "/etc/emulationstation/themes/carbon/moonlight/")
# cp ./themes/carbon/moonlight/art/* to /etc/emulationstation/themes/carbon/moonlight/art/
shutil.copy2("./themes/carbon/moonlight/art/*", "/etc/emulationstation/themes/carbon/moonlight/art/")