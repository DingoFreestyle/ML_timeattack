const imageInput = document.getElementById("imageUpload");

imageInput.onchange = () => {
    const selectedimage = imageInput.files[0]
    console.log(selectedimage);
};

/////////////////////////////////////////////////////////////////////

function preview(event) {
    var reader = new FileReader();

    reader.onload = function (event) {
        var img = document.createElement("img");
        img.setAttribute("src", event.target.result);
        document.querySelector("div#preciew_box").appendChild(img);
    };

    reader.readAsDataURL(event.target.files[0]);
}
