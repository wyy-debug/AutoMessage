# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['main.py','./src/device/device.py','./src/message/message.py',
              './src/number/number.py','./src/utils/httphandle.py','./src/devicemanage.py',
              './ui/untitled.py'],
             pathex=['./AutoMessageDes'],
             binaries=[],
             datas=[('src','src'),('ui','ui'),('src/device','src/device'),('src/message','src/message'),('src/number','src/number'),('src/utils','src/utils')],
             hiddenimports=[],
             hookspath=[],
             hooksconfig={},
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='main',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None )
