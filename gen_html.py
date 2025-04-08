import os

def parse_release_info(release_info_path):
    """
    Parse the release_info.txt to extract the release date, version, and Selenium version.
    """
    release_date = version = selenium_version = ""
    with open(release_info_path, 'r') as file:
        for line in file:
            if line.startswith("RELEASE"):
                release_date = line.split(':')[1].strip()
            elif line.startswith("VERSION"):
                version = line.split(':')[1].strip()
            elif line.startswith("SELENIUM_VERSION"):
                selenium_version = line.split(':')[1].strip()

    return release_date, version, selenium_version

def generate_index_html(base_path, output_path):
    """
    Generate an index HTML file listing all versions and their metadata.
    """
    # Start HTML structure
    html_content = """
    <html>
    <head>
        <title>Dobby Web Common Library</title>
    </head>
    <body>
        <h1>Dobby Web Common Library</h1>
        <table border="1">
            <tr>
                <th>Version</th>
                <th>Required Python</th>
                <th>Release Date</th>
                <th>Link</th>
            </tr>
    """

    # Loop through versions (directories)
    for version_folder in os.listdir(base_path):
        version_folder_path = os.path.join(base_path, version_folder)
        if os.path.isdir(version_folder_path):  # Make sure it’s a directory (version folder)
            release_info_path = os.path.join(version_folder_path, 'release_info.txt')
            if os.path.exists(release_info_path):
                release_date, version, selenium_version = parse_release_info(release_info_path)
                keyword_file = version + '.html'
                keyword_html_path = os.path.join(version_folder_path, keyword_file)
                print(keyword_html_path)
                # Add row to HTML table for this version
                html_content += f"""
                <tr>
                    <td>{version}</td>
                    <td>{selenium_version}</td>
                    <td>{release_date}</td>
                    <td onclick="location.href='keywords/{version}/keyword.html'">Keyword</td>
                </tr>
                """
    
    # End HTML structure
    html_content += """
        </table>
    </body>
    </html>
    """

    # Write the generated HTML to the output file
    with open(output_path, 'w', encoding='utf-8') as file:
        file.write(html_content)

    print(f"Index HTML generated at {output_path}")

# Specify the base path for versions and the path where the index will be saved
base_path = './keywords'  # This is the root folder containing version directories
output_path = 'index.html'  # Output file for the index page

generate_index_html(base_path, output_path)