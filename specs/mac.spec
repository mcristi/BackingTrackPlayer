# -*- mode: python -*-

import os

project_root = os.path.join(os.path.abspath(SPECPATH), '..')
app_name = 'Backing Track Player'
mac_icon = os.path.join(project_root, 'assets', 'icon.icns')


a = Analysis([os.path.join(project_root, 'main.py')],
             pathex=[project_root],
             binaries=[(os.path.join(project_root, 'bin', 'ffmpeg'), 'bin')],
             datas=[(os.path.join(project_root, 'assets', '*.png'), '.')],
             hiddenimports=['mido.backends.rtmidi'],
             hookspath=[],
             runtime_hooks=[],
             excludes=['_tkinter', 'Tkinter', 'enchant', 'twisted'],
             noarchive=False)

pyz = PYZ(a.pure, a.zipped_data)

exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name=app_name,
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=False,
          console=False,
          target_arch='arm64')

coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=False,
               name=app_name)

app = BUNDLE(coll,
             name=app_name + '.app',
             icon=mac_icon,
             bundle_identifier='com.backingtrackplayer.app')
