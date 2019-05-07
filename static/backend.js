function myscript(){
    var x = document.getElementById("myText").value;

    $.ajax('/firstclick', { data: {x: x },
        type: "POST",
        error: function() {
            alert("error");
        },
        success: function(data) {
            var div = document.createElement("div");
            div.innerHTML = data;
            document.getElementById("main").appendChild(div);

            var input = document.createElement("input");
            input.id = "myText2"
            input.type = "text";
            document.getElementById("main").appendChild(input);

            btn.onclick = myscript2;
        }
    });
}

function myscript2() {
    var x = document.getElementById("myText").value;
     var y = document.getElementById("myText2").value;

    $.ajax('/secondclick', { data: {x: x , y: y},
        type: "POST",
        error: function() {
            alert("error");
        },
        success: function(data) {
            split = JSON.parse(data)
            if (split['type'] == "input") {
                for (i=0; i<split['questions'].length; i++){
                    var div = document.createElement("div");
                    div.innerHTML = split['questions'][i];
                    document.getElementById("main").appendChild(div);

                    var input = document.createElement("input");
                    input.id = "myText" + (i+3)
                    input.type = "text";
                    document.getElementById("main").appendChild(input);
                }

                btn.onclick = myscript3;
            }
            else {

                var div = document.createElement("div");
                div.innerHTML = split['answer'];
                document.getElementById("main").appendChild(div);
            }

        }
    });
}

function myscript3(){
    queslen = split['questions'].length;
    jstext = {blob: document.getElementById("myText").value, answers: []};
    for (i=0; i<queslen; i++){
        jstext['answers'].push(document.getElementById("myText" + (i+3)).value)
    }

    var x = document.getElementById("myText").value;
     var y = document.getElementById("myText2").value;

    $.ajax('/thirdclick', { data: {x:x, y: y, js: JSON.stringify(jstext)},
        type: "POST",
        error: function() {
            alert("error");
        },
        success: function(data) {
            var div = document.createElement("div");
            div.innerHTML = data;
            document.getElementById("main").appendChild(div);
        }
    });
}

var div = document.createElement("div");
div.innerHTML = "Paste or type text that you would like to analyze here: ";

var input = document.createElement("input");
input.id = "myText"
input.type = "text";
document.getElementById("main").appendChild(input);

var btn = document.createElement("BUTTON");   // Create a <button> element
btn.innerHTML = "Submit";                   // Insert text
btn.onclick = myscript;
document.body.appendChild(btn);

document.getElementById("main").appendChild(div);
