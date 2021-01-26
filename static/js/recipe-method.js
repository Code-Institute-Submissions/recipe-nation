let counter2 = 2;
let limit2 = 30;
const newMethod = '<div id="methodholder*" class="input-field col s12"><i class="fas fa-wrench prefix"></i><input id="method*" type="text" name="method" minlength="3" maxlength="250" class="validate" required><label for="method*" placeholder="Step">Step *</label><a class="waves-effect waves-light btn" onClick="deleteMethod(this)" data-method="methodholder*"><i class="fas fa-times"></i> Remove</a></div>'

function deleteMethod(el) {
    console.log(el.getAttribute("data-method"));
    document.getElementById(el.getAttribute("data-method")).remove();
}
function addMethod(divName) {
    if (counter2 === limit2) {
        alert("You have reached the limit of adding " + counter2 + " steps");
    }
    else {
        console.log("Adding Method")
        let newdiv = document.createElement('div');
        newdiv.innerHTML = newMethod.replaceAll("*", counter2);
        document.getElementById(divName).appendChild(newdiv);
        counter2++;
    }
};
