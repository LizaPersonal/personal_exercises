
import urllib.request


class GeneralError(Exception):
    pass


def new_york_times_defined_values():
    link = "https://www.nytimes.com/"
    title_indicator = 'class="story-heading"'
    header_link_start = '<a href="'
    header_link_end = '</a>'
    link_end = 'class="region c-column-middle-span-region"'
    return link, title_indicator, header_link_start, header_link_end, link_end

header_array = []
header_index = 0
counter = 0
index = 0

response = urllib.request.urlopen(link)
front_page = str(response.read())
front_page_end = front_page.find(text_end)
total_headers = front_page.count(title_indicator, 0, front_page_end)

for counter in range(total_headers):
    header_index = front_page.find(title_indicator, header_index)
    header_array.append(header_index)
    counter += 1
    header_index += 1

while index < len(header_array):
    print(front_page[front_page.find(header_link_start, header_array[index]):(front_page.find(header_name_end, header_array[index]) + 4)])
    index += 1

