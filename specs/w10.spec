# -*- mode: python -*-

import os
from kivy_deps import sdl2, glew

project_root = os.path.join(os.path.abspath(SPECPATH), '..')
app_name = 'Backing Track Player'
win_icon = os.path.join(project_root, 'assets', 'icon.ico')

a = Analysis([os.path.join(project_root, 'main.py')],
             pathex=[project_root],
             binaries=[(os.path.join(project_root, 'bin', 'ffmpeg.exe'), 'bin')],
             datas=[(os.path.join(project_root, 'assets', '*.png'), '.')],
             hiddenimports=['mido.backends.rtmidi'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
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
          icon=win_icon)
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               *[Tree(p) for p in (sdl2.dep_bins + glew.dep_bins)],
               strip=False,
               upx=False,
               name=app_name)
