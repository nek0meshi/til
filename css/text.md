# CSS Text

## ellipsis

### 複数行の場合

```scss
.ellipsis {
    overflow: hidden;
    position: relative;
    line-height: 1.2em;
    max-height: 3.6em;
    padding-right: 1rem;
    text-align: justify;

    &::before {
        content: '...';
        position: absolute;
        right: 0;
        bottom: 0;
        background-color: #fff;
        width: 1rem;
    }

    &::after {
        content: '';
        position: absolute;
        right: 0;
        width: 1rem;
        height: 1.2em;
        background-color: #fff;
    }
}
```
※ 参考サイトとの差異として、`padding-right: 1rem;`を指定している。半角文字の対応のため。

参考： https://note.com/oceant/n/ncf25a3871d5d

## Misc.

### 縦書き

```css
-webkit-writing-mode: vertical-rl;
-ms-writing-mode: tb-rl;
writing-mode: vertical-rl;

```
https://qiita.com/RinoTsuka/items/3e3eaaba8cddb6ff08e9
