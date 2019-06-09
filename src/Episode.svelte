<script>
    export let id;
    export let date;
    export let title;
    export let file;
    export let base_url = "https://boggle.sfo2.digitaloceanspaces.com/the-bugle";
</script>

<style>
    .id {
        grid-column: 1;
        align-self: center;
    }
    .title {
        grid-column: 2;
        align-self: center;
    }
    .play {
        grid-column: 4;
        background: rgb(16, 159, 16);
        text-align: center;
        color: white;
        padding: 4px 8px;
        align-self: center;
        border-radius: 6px;
    }
    a {
        color: white;
        text-decoration: none;
    }
    a:hover, a:focus {
        background-color: #f1582d;
    }
    a:visited {
        background-color: darkgray;
    }
</style>

    <span class="id">{ id }</span>
    <span class="title">{ title }</span>
    <a class="play" aria-label="Play episode { id}: { title }" href="{base_url}/{ file }">Play</a>
