#!/bin/bash

get_github_pages_url() {
    # Get the remote URL of the 'origin' remote
    remote_url=$(git remote -v | grep '^origin' | grep '(fetch)' | awk '{print $2}')

    # Check if the remote URL is in SSH or HTTPS format
    if [[ $remote_url == git@github.com:* ]]; then
        # SSH format
        repo_name=$(echo $remote_url | sed 's/git@github.com://;s/\.git$//')
    elif [[ $remote_url == https://github.com/* ]]; then
        # HTTPS format
        repo_name=$(echo $remote_url | sed 's/https:\/\/github.com\///;s/\.git$//')
    else
        echo "Error: Not a GitHub repository or unsupported URL format."
        return 1
    fi

    # Construct GitHub Pages URL
    user_name=$(echo $repo_name | cut -d'/' -f1)
    repo_name=$(echo $repo_name | cut -d'/' -f2)
    echo "https://$user_name.github.io/$repo_name"
}

(
export PATH=$PATH:/home/juniorit/.local/bin

[ ! -f "/home/juniorit/.local/bin/pygbag" ] && pip3 install -r requirements.txt
#! command -v ffmpeg &> /dev/null && sudo apt-get update && sudo apt-get install -y ffmpeg --no-install-recommends
! command -v xdg-open &> /dev/null && sudo apt-get update && sudo apt-get install -y xdg-utils --no-install-recommends

case $1 in
    "clean")
        rm -rf mygame/build
        echo "Cleaned  mygame/build folder"
        exit 0
        ;;
    "web")
        php -S localhost:9000 -t mygame/build/web
        exit 0
        ;;
    "debug")
        xdg-open http://localhost:9000?-i; php -S localhost:9000 -t mygame/build/web
        exit 0
        ;;
    "local_dev")
        python3 -m pygbag --bind localhost --port 9000 mygame
        exit 0
        ;;
    "deploy")
        cp -f mygame/build/web/*.* "$GAMECRAFT_PROJECT_PATH/python/"
        cd $GAMECRAFT_PROJECT_PATH
        git add .
        git commit -a -m "deploy at $(date)"
        git push
        echo
        echo "Your game has been deployed to `get_github_pages_url`, and you can share with your friends now."
        echo
        cd -
        exit 0
        ;;
    "submit")
        juniorit submit
        exit 0
        ;;
    *)
        # for the rest
        ;;
esac

[ ! -f "mygame/build/web/archives" ] && (mkdir -p mygame/build/web; ln -s `pwd`/pygame-web mygame/build/web/archives)
pygbag --build --ume_block 0 --cdn https://pygame-web.github.io/archives/0.8/ --title "JuniorIT.AI - Game Craft" --app_name "JuniorIT.AI - Game Craft"  ./mygame/main.py

)
