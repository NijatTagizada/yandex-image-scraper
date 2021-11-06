import csv

csv_file = open('failed_links.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Links'])


def export_failed_links(failed_url_list):
    for i in failed_url_list:
        csv_writer.writerow([i])
    csv_file.close()
