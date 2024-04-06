from engines.models import Engine

all_engines = [
      'alibaba', 'apertium', 'argos', 'baidu', 'bing',
    'caiyun', 'cloudTranslation', 'deepl', 'elia', 'google',
    'hujiang', 'iciba', 'iflytek', 'iflyrec', 'itranslate',
    'judic', 'languageWire', 'lingvanex', 'mglip', 'mirai',
    'modernMt', 'myMemory', 'niutrans', 'papago', 'qqFanyi',
    'qqTranSmart', 'reverso', 'sogou', 'sysTran', 'tilde',
    'translateCom', 'translateMe', 'utibet', 'volcEngine', 'yandex',
    'yeekit', 'youdao',
]
print(len(all_engines))
def run():
    for item in all_engines:
        new_engine = Engine(title=item)
        new_engine.save()
        print("weng")
        print(f"{new_engine}--saved")

if __name__ == "__main__":
    run()