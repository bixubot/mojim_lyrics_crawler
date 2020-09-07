# Mojim Lyrics Crawler

## Description

- Python Crawler built to parse lyrics from Mojim.com for the purpose of gathering research data. The data can be used to train models such as GPT-2 for Chinese.
- 用Python为魔镜歌词网(Mojim.com)设计的歌词爬虫。目的是提供一个收集中文歌词语料的工具，以便小伙伴们从事GPT-2一类基于Transformer的语言模型的研究。

## How to use

- Simply run `crawler.py` from the root directory.
- 在项目根目录运行`crawler.py`即可。

``` bash
python ./crawler.py
```

## Files generated

- The `crawler.py` will parse down all lyrics for the singers that are listed in sectional ranking of sections *Asian male*, *Asian female*, and *Asian group*. The lyrics are processed and grouped by singers. They will be stored in their respective `txt` files under the directory `./lyrics/`. In total, there will be 240 singers/groups in the collection.
- `crawler.py`将会从*华语男生*，*华语女生*，和*华语团体*三大分类的本区排行的所有歌手中，爬取其所有歌曲的歌词。爬取的歌词会被简单预处理，除去一些多余内容后，根据歌手名称存在`lyrics`下的`txt`文件里。其中包括240个歌手或团体。

## Before you start

- Note that this project should only be used for research purpose and not for any profitable usage. Please respect the copyrights of the lyrics.
- 本项目仅供学习使用，请尊重版权，请勿利用此项目从事商业行为！
