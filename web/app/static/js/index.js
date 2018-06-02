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
          // clear all poem_para
          if(document.getElementById("poem_para")){
            parent = document.getElementById("poem")
            son = document.getElementById("poem_para");
            while(son){
              parent.removeChild(son);
              son = document.getElementById("poem_para");
              console.log("delete")
            }
          }

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
$(function(){
	$("#but-keyword").click(function(){
    $.ajax({
        url: "/word",
        data: {},
        dataType: 'json',
        success: function(data) {
					console.log(data);
					keywords = data["keywords"];
					var result = " ";
					for(var i=0;i<keywords.length;i++){
						keyword = keywords[i];
						//console.log(keyword);
						result = result + keyword + " ";

					}
					document.getElementById("p-keyword").innerText = result;

				}
			});
		});
})
poem_new = '';
$(function(){
		$("#but-text").click(function(){
	    $.ajax({
	        url: "/longtext",
	        data: {},
	        dataType: 'json',
	        success: function(data) {
						console.log(data);
						longtext = data["longtext"];
						poem = data["poem"];
						poem_new = poem;
						start = 0;
						for(var text in longtext){
							console.log(text);
							insert_index = poem_new.indexOf(text) + text.length;
							console.log(insert_index);
							end = poem_new.length;
							poem_tmp_1 = poem_new.substring(start, insert_index);
							poem_tmp_2 = poem_new.substring(insert_index, end);
							insert_str = longtext[text];
							poem_new = poem_tmp_1 +''+ insert_str + poem_tmp_2;
						}
						console.log(poem_new);
						$.ajax({
								type:'POST',
								data:JSON.stringify({"poem":poem_new}),
								contentType: 'application/json; charset=UTF-8',
								dataType:'json',
								url:'/newpoem',
								async: false,
								success:function(data){
									      alert("ok");
						            // alert(JSON.stringify({"poem":poem_new}));
						            // alert(data['poem'])
						        }
							});
					  document.getElementById("p-text").innerText = poem_new;
					}
				});
		});
		// $.ajax({
		// 		type:'POST',
		// 		data:JSON.stringify({"poem":poem_new}),
		// 		contentType: 'application/json; charset=UTF-8',
		// 		dataType:'json',
		// 		url:'/type',
		// 		success:function(data){
		// 			      alert("ok");
		//             alert(JSON.stringify({"poem":poem_new}));
		//             alert(data['poem'])
		//         }
		// 	});
})
$(function(){
	$("#but-class").click(function(){
    $.ajax({
        url: "/type",
        data: {},
        dataType: 'json',
        success: function(data) {
					console.log(data);
					result = data["type"];
					document.getElementById("p-class").innerText = result;

				}
			});
		});
})
