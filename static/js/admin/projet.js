add = document.getElementById("section-add");
form = document.getElementById("sections-form");

index = document.getElementsByClassName("porjet-field-section").length;

deletes = document.getElementsByClassName("delete");
Array.from(deletes).forEach(d => {
    d.addEventListener("click", e => {
        e.preventDefault();
        d.parentElement.remove();
    });
});

add.addEventListener("click", e => {
    e.preventDefault();
    index += 1;
    form.innerHTML += `
    <fieldset class="projet-field projet-field-section" id="section-` + index + `">
        <label for="title-` + index + `">Titre</label>
        <input type="text" name="title-` + index + `" />
        <label for="content-` + index + `">Contenu</label>
        <textarea rows="10" name="content-` + index + `">
            
        </textarea>
        <button id="delete-` + index + `" class="delete">Supprimer</button>
    </fieldset>
    `;
    document.getElementById("delete-" + index).addEventListener("click", e => {
        e.preventDefault();
        document.getElementById("section-" + index).remove();
    });
});