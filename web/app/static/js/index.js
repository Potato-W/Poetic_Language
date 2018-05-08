$(function(){
	$("#random").click(function(){
    $.ajax({
        url: "/poem",
        data: {},
        dataType: 'json',
        success: function(data) {
          console.log(data);
          console.log(data["poem"])
          data = data["poem"]
          poem_title = data[0]
          poem_author = data[1]
          poem_para = data[2]
          document.getElementById("poem_title").innerText = poem_title
          document.getElementById("poem_author").innerText = poem_author
          var length = poem_para.length
          console.log(length)
          for(var i=0;i<length;i++){
            var poem_item = document.createElement("p");
            poem_item.id="poem_para";
            poem_item.innerHTML=poem_para[i];
            document.getElementById("poem").appendChild(poem_item);
          }
        },
        error: function(xhr, type) {
        }
    });

  });
})
