import React from "react";
import "../CSS/Walkthroughs.css";

const Walkthroughs = () => {
    const cardData = [
        {
            imageSrc: "https://analisadaily.com/imagesfile/202211/20221129-192005_valorant-akan-segera-hadir-di-android.jpeg",
            songName: "Valorant",
            link: "https://www.youtube.com/watch?v=S-rxwnC7ygg",
        },
        {
            imageSrc: "https://www.infobae.com/new-resizer/V0V3FmYGrNvy9mPrzhqjJ0BFMKg=/filters:format(webp):quality(85)/cloudfront-us-east-1.images.arcpublishing.com/infobae/AKOWAE227JGRFEHUHTCNVT7RZM.jpg",
            songName: "League of Legends",
            link: "https://leagueoflegends.fandom.com/wiki/Tutorial_(League_of_Legends)",
        },
        {
            imageSrc: "https://m.media-amazon.com/images/M/MV5BZWVlMDAxMjUtMWYwYS00MGU4LTgxYWEtZGE2NjZiMTU3YjRmXkEyXkFqcGdeQXVyNjU1OTg4OTM@._V1_FMjpg_UX1000_.jpg",
            songName: "TeamFight Tactics",
            link: "https://mobalytics.gg/blog/tft-guide/",
        },
        {
            imageSrc: "https://media.contentapi.ea.com/content/dam/apex-legends/images/2019/01/apex-featured-image-16x9.jpg.adapt.crop16x9.1023w.jpg",
            songName: "Apex Legends",
            link: "https://www.youtube.com/watch?v=UEwTnirimf0",
        },
        {
            imageSrc: "https://static.invenglobal.com/upload/image/2020/05/11/o1589232897513893.jpeg",
            songName: "Counter Strike: Global Offensive",
            link: "https://www.esports.com/en/a-beginners-guide-to-csgo-180270",
        },
        {
            imageSrc: "https://cdn.akamai.steamstatic.com/steam/apps/730/capsule_616x353.jpg?t=1696283405",
            songName: "Counter Strike: 2",
            link: "https://www.youtube.com/watch?v=Go0K9BuQxa8",
        },
        {
            imageSrc: "https://image.api.playstation.com/vulcan/ap/rnd/202305/1523/5aaaa377b9a4803f932a1aa4f4b18d8b12ca7c29490dfb14.jpg",
            songName: "Brawlhalla",
            link: "https://www.youtube.com/watch?v=tSsWJHXeolk",
        },
        {
            imageSrc: "https://assets.nintendo.com/image/upload/c_fill,w_1200/q_auto:best/f_auto/dpr_2.0/ncom/software/switch/70010000012332/ac4d1fc9824876ce756406f0525d50c57ded4b2a666f6dfe40a6ac5c3563fad9",
            songName: "Super Smash Bros",
            link: "https://www.smashbros.com/en_US/howtoplay/index.html",
        },
        {
            imageSrc: "https://assets1.ignimgs.com/2019/05/31/mario-kart-8-deluxe---button-1559265583166.jpg",
            songName: "Mario Kart 8",
            link: "https://www.youtube.com/watch?v=r0Xfn3Bq3X8",
        },
        {
            imageSrc: "https://cdn.cloudflare.steamstatic.com/steam/apps/814380/capsule_616x353.jpg?t=1678991267",
            songName: "Sekiro: Shadows Die Twice",
            link: "https://www.youtube.com/watch?v=zp4wYsGU78M",
        },
        {
            imageSrc: "https://image.api.playstation.com/vulcan/ap/rnd/202110/2000/aGhopp3MHppi7kooGE2Dtt8C.png",
            songName: "Elden Ring",
            link: "https://www.youtube.com/watch?v=PN7YFKHOR9Y",
        },
        {
            imageSrc: "https://cdn1.epicgames.com/min/offer/2560x1440-2560x1440-5e710b93049cbd2125cf0261dcfbf943.jpg",
            songName: "Hades",
            link: "https://www.youtube.com/watch?v=mbEprwGIrLw",
        },
    ];

    return (
        <div className="center-content">
            <h1>Level Up Your Skills: Game Tutorials and Tips</h1>
            <div className="card-container">
                {cardData.map((card, index) => (
                    <div key={index} className="card">
                        <img src={card.imageSrc} alt={card.songName} />
                        <h3>{card.songName}</h3>
                        <a href={card.link}>Learn More</a>
                    </div>
                ))}
            </div>
        </div>
    );
};

export default Walkthroughs;
