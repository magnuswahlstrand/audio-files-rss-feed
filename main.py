import datetime
import os
from xml.dom.minidom import parseString
from xml.etree.ElementTree import Element, SubElement, tostring

durations = [
    334.106063,
    478.772187,
    374.883250,
    508.891375,
    564.793437,
    424.960000,
    615.157500,
    453.328937,
    548.048937,
    747.911812,
    652.277500,
    833.802437,
    577.959125,
    910.393438,
    540.029375,
    458.501188,
    802.664437,
    410.906063,
    422.034250,
    561.841625,
    733.257125,
    790.726500,
    418.690562,
    344.607312,
    727.484063,
    524.486500,
    645.511813,
    682.501188,
    527.203250,
    450.586063,
    420.101187,
    580.048937,
    523.650562,
    546.899563,
    341.786063,
    663.013875,
    799.947750,
    564.845688,
    635.141188,
    759.771375,
    786.729750,
    424.385250,
    545.515062,
    607.033437,
    771.631000,
    650.344438,
    575.477500,
    660.114250,
    649.586937,
    563.330563,
    740.022812,
    870.504437,
    498.991000,
    582.974687,
    939.520000,
    824.189375,
    689.998312,
    548.989375,
    643.134688,
    506.070187,
    479.294688,
    713.142812,
    298.344438,
    804.205687,
    906.240000,
    297.926500,
    703.111813,
    489.534688,
    569.808937,
    658.468562,
    760.502813,
    780.643250,
    483.787750,
    547.813875,
    560.195875,
    490.997500,
    415.268562,
    563.957500,
    429.635875,
    429.609750,
    716.382000,
    404.035875,
    491.232625,
    472.372187,
    291.683250,
    538.749375,
    617.822000,
    577.802437,
    497.867750,
    413.126500,
]


def duration(seconds):
    return str(datetime.timedelta(seconds=seconds))


def generate_rss_feed(audio_files):
    # Basic podcast metadata
    podcast_title = "Language Transfer - Spanish"
    podcast_link = "https://www.languagetransfer.org/free-courses-1#complete-spanish"
    podcast_language = "es-es"
    podcast_subtitle = "Unofficial feed"
    podcast_author = "Unofficial feed creator"
    podcast_summary = "Language Transfer - Spanish Course. Unofficial feed."
    podcast_description = "Language Transfer"
    podcast_category = "Education"
    # podcast_email = "Your Email"
    podcast_image = "https://storage.googleapis.com/language-transfer/unofficial_language_transfer.webp"

    # Create the root element
    rss = Element('rss')
    rss.set('version', '2.0')
    rss.set('xmlns:itunes', 'http://www.itunes.com/dtds/podcast-1.0.dtd')
    rss.set('xmlns:content', 'http://purl.org/rss/1.0/modules/content/')
    rss.set('xmlns:atom', 'http://www.w3.org/2005/Atom')


    channel = SubElement(rss, 'channel')
    SubElement(channel, 'title').text = podcast_title
    SubElement(channel, 'link').text = podcast_link
    SubElement(channel, 'language').text = podcast_language
    SubElement(channel, 'itunes:subtitle').text = podcast_subtitle
    SubElement(channel, 'itunes:author').text = podcast_author
    SubElement(channel, 'itunes:summary').text = podcast_summary
    SubElement(channel, 'description').text = podcast_description
    SubElement(channel, 'itunes:explicit').text = 'no'  # Or 'yes' or 'clean' depending on your content

    itunes_owner = SubElement(channel, 'itunes:owner')
    SubElement(itunes_owner, 'itunes:name').text = podcast_author
    # SubElement(itunes_owner, 'itunes:email').text = podcast_email
    SubElement(channel, 'itunes:image', href=podcast_image)
    SubElement(channel, 'itunes:category', text=podcast_category)

    # Add episodes
    for i, audio_url in enumerate(audio_files, start=1):
        item = SubElement(channel, 'item')
        SubElement(item, 'title').text = f"Episode {i}"
        SubElement(item, 'itunes:author').text = podcast_author
        SubElement(item, 'itunes:subtitle').text = f"Episode {i} subtitle"
        SubElement(item, 'itunes:summary').text = f"Episode {i} summary."
        SubElement(item, 'itunes:image', href=podcast_image)
        SubElement(item, 'enclosure', url=audio_url, length="1234567", type="audio/mpeg")
        SubElement(item, 'guid').text = audio_url
        SubElement(item, 'pubDate').text = datetime.datetime.utcnow().strftime("%a, %d %b %Y %H:%M:%S GMT")
        SubElement(item, 'itunes:duration').text = duration(int(durations[i - 1]))
        # SubElement(item, 'itunes:duration').text = "00:30:00"  # Example duration, adjust as needed

    # Generate the XML string and pretty print it
    rough_string = tostring(rss, 'utf-8')
    reparsed = parseString(rough_string)
    pretty_xml_as_string = reparsed.toprettyxml(indent="  ")

    # Write to file
    with open("podcast_feed.xml", "w") as f:
        f.write(pretty_xml_as_string)


# Example list of audio file URLs
storage_prefix = os.environ.get("STORAGE_PREFIX")
audio_files = [storage_prefix + str(i).rjust(2, "0") + ".mp3" for i in range(1, 90 + 1)]

generate_rss_feed(audio_files)