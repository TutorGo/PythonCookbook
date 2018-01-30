# 2-17 HTML과 XML 엔티티 처리

## 문제

&entity;나 &#code;와 같은 HTML, XML 엔티티를 이에 일치하는 문자로 치환하고 싶다. 혹은 텍스트를 생성할 떄 특정 문자(<, >, & 등)를 피하고 싶다.

## 해결

텍스트를 생성할 떄 <나>와 같은 특수 문자를 치환하는 것은 html.escape() 함수를 사용하면 상대적으로 간단히 처리할 수 있다.

```
In [123]: s = 'Elements are written as "<tag>text</tag>.'

In [124]: import html

In [125]: s
Out[125]: 'Elements are written as "<tag>text</tag>.'

In [126]: html.escape(s)
Out[126]: 'Elements are written as &quot;&lt;tag&gt;text&lt;/tag&gt;.'


# 따옴표는 남겨 두도록 지정
In [127]: html.escape(s, quote=False)
Out[127]: 'Elements are written as "&lt;tag&gt;text&lt;/tag&gt;.'
```

텍스트를 아스키로 만들고 캐릭터 코드를 아스키가 아닌 문자에 끼워 넣고 싶으면 errors='xmlcharrefreplace' 인자를 입출력 관련 함수에 사용한다.

```
In [128]: s = 'Spicy Jalapeño'

In [129]: s.encode('ascii', errors='xmlcharrefreplace')
Out[129]: b'Spicy Jalape&#241;o'
```

텍스트의 엔티티를 치환하면 또 다른 처리를 해야 한다. 실제로 HTML, XML을 처리할 예정이면 우선 올바른 HTML, XML 파서를 사용하도록 한다. 일반적으로 이런 도구는 파싱하는 동안 자동으로 값을 치환해 준다.

하지만 어쨰서인지 자동으로 처리되지 않았고 수동으로 치환을 해야 한다면 HTML, XML파서에 내장되어 있는 여러 유틸리티 함수나 메소드를 사용한다.

```
In [130]: s = 'Spicy &quot;Jalape&#241;o&quot.'

In [134]: html.unescape(s)
Out[134]: 'Spicy "Jalapeño".'

In [135]: t = 'The prompt is &gt;&gt;&gt;'

In [136]: from xml.sax.saxutils import unescape

In [137]: unescape(t)
Out[137]: 'The prompt is >>>'
```

HTML, XML을 생성할 때 특수 문자를 제대로 이스케이핑하는 과정을 간과하기 쉽다. print()로 결과물을 생성하거나 기본적인 문자열 서식 기능을 사용할 때 특히 더 그렇다. 가장 쉬운 해결책은 html.escape()와 같은 유틸리티 함수를 사용하는 것이다.

또 다른 방시으로 텍스트를 처리하고 싶다면 xml.sax.saxutils.unescape()와 같은 여러 유틸리티 함수가 도움이 된다. 하지만 올바른 파서 사용법을 익히는 것이 훨씬 중요하다. 예를 들어 html.parser나 xml.etree.ElementTree와 같은 파싱 모듈로 HTML, XML을 처리하면 엔티티 치환과 같은 기본적인 내용을 아아서 다 처리해 준다

