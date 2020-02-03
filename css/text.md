# CSS Text

## ellipsis

### 複数行の場合

```scss
.ellipsis {
    overflow: hidden;
    position: relative;
    line-height: 1.2em;
    max-height: 3.6em;
    text-align: justify;

    &::before {
        content: '...';
        position: absolute;
        right: 0;
        bottom: 0;
        background-color: #fff;
        width: 1em;
    }

    &::after {
        content: '';
        position: absolute;
        right: 0;
        width: 1em;
        height: 1.2em;
        background-color: #fff;
    }
}
```
参考： https://note.com/oceant/n/ncf25a3871d5d

## Misc.

### 縦書き

```css
-webkit-writing-mode: vertical-rl;
-ms-writing-mode: tb-rl;
writing-mode: vertical-rl;

```
https://qiita.com/RinoTsuka/items/3e3eaaba8cddb6ff08e9
