ws = new WebSocket("ws://site.com/demo");

// навешиваем на новый объект три колл-бека:

// первый вызовется, когда соединение будет установлено:
ws.onopen = function() { alert("Connection opened...") };

// второй — когда соединено закроется
ws.onclose = function() { alert("Connection closed...") };

// и, наконец, третий — каждый раз, когда браузер получает какие-то данные через веб-сокет
ws.onmessage = function(evt) {$("#msg").append("<p>"+evt.data+"</p>"); };