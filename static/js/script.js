const toggleSubmitButton = (flag) => {
    document.getElementsByClassName('upload-btn')[0].disabled = !flag;
};

const checkFileType = (event) => {
    event.preventDefault();
    console.log(event.target.files[0]);
    if (!event?.target?.files?.length === 0) {
        toggleSubmitButton(false);
        document.getElementsByClassName('error-message')[0].innerHTML = 'File not found';
        return;
    }

    if (event.target.files[0].size > 2*1024*1024) {
        toggleSubmitButton(false);
        document.getElementsByClassName('error-message')[0].innerHTML = 'File size must be less than 2MB';
        return;
    }
    if (!['application/vnd.ms-excel', 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'].includes(event.target.files[0].type)) {
        toggleSubmitButton(false);
        document.getElementsByClassName('error-message')[0].innerHTML = 'Only .xlsx/.xls files are allowed';
        return;
    }
    toggleSubmitButton(true);
};

document.getElementsByClassName('upload-form')[0].addEventListener('submit', async (event) => {
    event.preventDefault();
    await fetch('/add_product', {
        method: 'POST',
        body: new FormData(document.getElementsByClassName('upload-form')[0])
    }).then(function(response) {
        if (response.status == 200) {
            document.getElementsByClassName('error-message')[0].innerHTML = 'Upload successful';
        } else {
            document.getElementsByClassName('error-message')[0].innerHTML = response.statusText;
        }
        window.location.href = "/products";
    }).catch(function(error) {
        console.log(error);
    });
});

const search = (event) => {
    if (window.location.href.includes('q')) {
        window.location.href = window.location.href.replace(/q=([^&#]*)/, `&q=${event.target.value}`);
    } else {
        if (window.location.href.includes('?')) {
            window.location.href += `&q=${event.target.value}`;
        } else {
            window.location.href += `?q=${event.target.value}`;
        }
    }
}

const sort = (column) => {
    if (window.location.href.includes('sortcol') && window.location.href.includes('sortdir')) {
        let dir = window.location.href.split('sortdir=')[1].split('&')[0];
        dir = (dir === 'asc' ? 'desc' : 'asc');
        window.location.href = window.location.href.replace(/sortcol=([^&#]*)/, `sortcol=${column}`).replace(/sortdir=([^&#]*)/, `sortdir=${dir}`);
    } else {
        if (window.location.href.includes('?')) {
            window.location.href += `&sortcol=${column}&sortdir=asc`;
        } else {
            window.location.href += `?sortcol=${column}&sortdir=asc`;
        }
    }
}

const changePage = (page) => {
    if (window.location.href.includes('page')) {
        window.location.href = window.location.href.replace(/page=([^&#]*)/, `page=${page}`);
    } else {
        if (window.location.href.includes('?')) {
            window.location.href += `&page=${page}`;
        } else {
            window.location.href += `?page=${page}`;
        }
    }
}