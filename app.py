from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/block_websites', methods=['POST'])
def block_websites():
    try:
        websites = request.form.get('websites')
        if websites:
            websites = websites.split(',')
            redirect = "127.0.0.1"

            hosts_path = get_hosts_path()
            
            # Check if the file is readable
            try:
                with open(hosts_path, 'r') as read_file:
                    content = read_file.read()
            except IOError as e:
                return jsonify({"status": "error", "message": f"Error reading the hosts file: {str(e)}"})

            # Check if the file is writable
            try:
                with open(hosts_path, 'a') as write_file:
                    for site in websites:
                        if site not in content:
                            write_file.write(redirect + " " + site + "\n")
            except IOError as e:
                return jsonify({"status": "error", "message": f"Error writing to the hosts file: {str(e)}"})

            return jsonify({"status": "success", "message": "Websites blocked"})
        else:
            return jsonify({"status": "error", "message": "Please provide websites to block"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

@app.route('/unblock_websites', methods=['POST'])
def unblock_websites():
    try:
        websites = request.form.get('websites')
        if websites:
            websites = websites.split(',')

            hosts_path = get_hosts_path()

            # Check if the file is readable
            try:
                with open(hosts_path, 'r') as read_file:
                    content = read_file.readlines()
            except IOError as e:
                return jsonify({"status": "error", "message": f"Error reading the hosts file: {str(e)}"})

            # Check if the file is writable
            try:
                with open(hosts_path, 'w') as write_file:
                    for line in content:
                        if any(site in line for site in websites):
                            continue
                        write_file.write(line)
            except IOError as e:
                return jsonify({"status": "error", "message": f"Error writing to the hosts file: {str(e)}"})

            return jsonify({"status": "success", "message": "Websites unblocked"})
        else:
            return jsonify({"status": "error", "message": "Please provide websites to unblock"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

def get_hosts_path():
    import platform

    if platform.system() == "Windows":
        return r"C:\Windows\System32\drivers\etc\hosts"
    elif platform.system() == "Linux":
        return r"/etc/hosts"
    elif platform.system() == "Darwin":
        return r"/private/etc/hosts"
    else:
        raise NotImplementedError("Unsupported operating system")

if __name__ == '__main__':
    app.run(debug=True)
