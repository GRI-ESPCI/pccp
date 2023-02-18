import bbcode

from pccp import app


def _render_img(name, value, options, parent, context):
    if "alt" in options:
        alt = options['alt']
        return f'<div class="projet-center"><img alt="{alt}" src="{value}" /></div>'
    return value

def _render_map(name, value, options, parent, context):
    if "bbox" in options and "marker" in options:
        bbox = options['bbox']
        marker = options['marker']
        marker_data = marker.split('%2C')
        return f'<div class="projet-center"><iframe width="425" height="350" frameborder="0" scrolling="no" marginheight="0" marginwidth="0" src="https://www.openstreetmap.org/export/embed.html?bbox={bbox}&amp;layer=mapnik&amp;marker={marker}" style="border: 1px solid black"></iframe><br/><small><a href="https://www.openstreetmap.org/?mlat={marker_data[0]}&amp;mlon={marker_data[1]}#map=16/47.6586/2.3446">Afficher une carte plus grande</a></small></div>'

    return value

def _text_formatting(name, value, options, parent, context):
    classes = ""
    style = ""
    if "center" in options:
        classes += "center "
    if "justify" in options:
        classes += "justify "
    if "size" in options:
        style += f"font-size={options['size']};"
    return f"<{name} class=\"{classes}\" style=\"{style}\">{value}</{name}>"

def parse_bbcode(data):
    parser = bbcode.Parser(newline="")
    parser.add_formatter('h1', _text_formatting)
    parser.add_formatter('h2', _text_formatting)
    parser.add_formatter('h3', _text_formatting)
    parser.add_formatter('p', _text_formatting)
    parser.add_formatter('b', _text_formatting)
    parser.add_formatter('i', _text_formatting)
    parser.add_formatter('u', _text_formatting)
    parser.add_simple_formatter('yt', '<div class="projet-center"><div class="projet-yt"><iframe class="projet-yt" width="560" height="315" src="https://www.youtube.com/embed/%(value)s" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></div></div>')
    parser.add_simple_formatter('ha', '<div class="projet-center"><iframe class="projet-ha" id="haWidget" allowtransparency="true" scrolling="auto" src="http://helloasso.com/%(value)s" onload="window.scroll(0, this.offsetTop)"></iframe></div>', replace_links=False)
    parser.add_formatter('img', _render_img, replace_links=False)
    parser.add_formatter('osm', _render_map, standalone=True)
    return parser.format(data)