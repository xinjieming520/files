# 视频资源配置中心

## 目录结构

```text
files/
├── source/
   └── LunaTV-config.json
├── video/
   ├── config_moontv.json
   ├── config_kvideo.json
   ├── config_moontv_base58.json
   └── tvbox.json

```

## 文件说明

1. `source/LunaTV-config.json`
源配置文件
2. `video/config_moontv.json`
由工作流复制生成
3. `video/config_kvideo.json`
由转换脚本从源配置转换得到的 KVideo 格式文件
4. `video/config_moontv_base58.json`
由编码脚本对源配置进行 Base58 编码得到
