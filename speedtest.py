import Python.speedtest as speedtest

def check_speed():
    test = speedtest.Speedtest()
    
    print("Loading server list...")
    test.get_servers()  # Get list of available servers
    
    print("Choosing best server...")
    best_server = test.get_best_server()  # Find the optimal server
    print(f"Found: {best_server['host']} ({best_server['country']})")
    
    print("Testing download speed...")
    download_speed = test.download() / 1_000_000  # Convert to Mbps
    print(f"Download Speed: {download_speed:.2f} Mbps")
    
    print("Testing upload speed...")
    upload_speed = test.upload() / 1_000_000  # Convert to Mbps
    print(f"Upload Speed: {upload_speed:.2f} Mbps")
    
    print("Speed test completed!")

check_speed()