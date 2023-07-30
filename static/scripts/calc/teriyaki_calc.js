function writ() {
    tbl = document.getElementById('tbl');
    main_ingredient = Math.round(document.getElementById("myNumber").value);

    for (var i = tbl.rows.length; i > 0; i--) {
        tbl.deleteRow(0);
    }

    addRow(tbl, 'Soy sauce', Math.round(main_ingredient) + ' ml', Math.round(main_ingredient) / 1000 + ' liter', Math.round(main_ingredient) / 250 + ' cup');
    addRow(tbl, 'Mirin', Math.round(main_ingredient / 1) + ' ml', Math.round(main_ingredient) / 1 / 1000 + ' liter', Math.round(main_ingredient) / 1 / 250 + ' cup');
    addRow(tbl, 'Sugar', Math.round(main_ingredient /2*3) + ' gr', Math.round(main_ingredient /2*3) / 1000 + ' kg', Math.round(main_ingredient /2*3) / 250 + ' cup');
}

function addCell(tr, val) {
    var td = document.createElement('td');
    td.innerHTML = val;
    tr.appendChild(td)
}

function addRow(tbl, val_1, val_2, val_3, val_4) {
    var tr = document.createElement('tr');
    addCell(tr, val_1);
    addCell(tr, val_2);
    addCell(tr, val_3);
    addCell(tr, val_4);
    tbl.appendChild(tr)
}