function xhrGet(url, callback) {
  var xhr = new XMLHttpRequest();
  xhr.onreadystatechange = function() { 
    if (xhr.readyState == 4 && xhr.status == 200)
      callback(xhr.responseText);
  }
  xhr.open("GET", url, true);
  xhr.send(null);
};

xhrGet('test.json', function(response) {
  var data = JSON.parse(response);
  var itemsDiv = document.getElementById('items')
  for(var i=0; i < data.length; i++) {
    item = '<div class="item"><a href="' + data[i]['url'] + '">' + data[i]['title'] + '</a></div>';
    itemsDiv.innerHTML = itemsDiv.innerHTML + item;
  }
});
