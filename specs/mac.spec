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
             excludes=['_tkinter', 'Tkinter', 'enchant', 'twisted',
                       'PIL', 'Pillow', 'ssl', '_ssl', 'hashlib'],
             noarchive=False)

# Remove unnecessary shared libraries that get pulled in as dependencies
# Keep libs required by the bundled ffmpeg binary (libav*, libsw*, libssl, libcrypto,
# libvpx, libdav1d, libmp3lame, libopus, libSvtAv1, libx264, libx265)
# Only exclude image/GUI libs not needed by this app
exclude_libs = {
    'libavif', 'libwebp', 'libsharpyuv', 'libbrotli', 'libharfbuzz',
    'libtiff', 'libopenjp2', 'liblcms2', 'libXau', 'libxcb',
}

a.binaries = [b for b in a.binaries
              if not any(b[0].startswith(prefix) for prefix in exclude_libs)]
a.datas = [d for d in a.datas if not d[0].startswith('PIL')]

pyz = PYZ(a.pure, a.zipped_data)

exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name=app_name,
          debug=False,
          bootloader_ignore_signals=False,
          strip=True,
          upx=False,
          console=False,
          target_arch='arm64')

coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=True,
               upx=False,
               name=app_name)

app = BUNDLE(coll,
             name=app_name + '.app',
             icon=mac_icon,
             bundle_identifier='com.backingtrackplayer.app')
