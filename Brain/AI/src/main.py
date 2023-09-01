import argparse
import os
from AI.src.ball_sort.helper import ball_sort
from AI.src.candy_crush.helper import candy_crush
from AI.src.webservices.helpers import require_image_from_url
import constants
import sys

if __name__ == '__main__':
    msg = "Description"
    
    parser = argparse.ArgumentParser(description=msg)
    parser.add_argument("-g", "--games", type=str, help="Name of the games", choices = ["ball_sort", "candy_crush"], required=True)
    parser.add_argument("-dV", "--debugVision", action="store_true", help="Debug screenshot")
    parser.add_argument("-t", "--test", type=str, help="screenshots to test prefix")
    parser.add_argument("-s", "--screenshot", type=str, help="specific screenshot path")
    
    args = parser.parse_args()
    
    
    def Start():
        if args.games == "ball_sort":
            ball_sort( screenshot,args.debugVision)
        elif args.games == "candy_crush":
            candy_crush(screenshot,args.debugVision)
    #game = parser.parse_args()
    #print (f"Taking first screenshot from {constants.SCREENSHOT_SERVER_IP}...")
    # TODO: change ip!
    
    if args.test == None:
        if not args.debugVision:
            server_ip, port = constants.SCREENSHOT_SERVER_IP, 5432
            try:
                require_image_from_url(server_ip, port)
                print("SCREENSHOT TAKEN.")
            except Exception as e:
                print(e)
        else:
            screenshot=""
            if args.screenshot == None:
                screenshot = args.games+"Test.jpg"
            else:
                screenshot = args.screenshot
            print("DEBUG MODE ON")   
            print(screenshot)
            Start()
    else:
        if args.games == "balls_sort":
            print("Screenshot\t#FullTubes\t#EmptyTubes\t#Balls\t#Colors", file=sys.stderr)
        for filename in os.listdir(constants.SCREENSHOT_PATH):
            if filename.startswith(args.test):
                screenshot = filename
                print(f"{screenshot}")
                print(f"{screenshot.split('.')[1]}\t",end='',file=sys.stderr)
                Start()
    
    
        