use elearning;

insert into vcategory(vcategory_name)
values('cloud'),('technology'),('development');

insert into video(video_name,video_link,vcategory_id)
values('Le cloud computing expliqué en 7 minutes','https://www.youtube.com/channel/UC5cs06DgLFeyLIF_II7lWCQ',1),
('XAVKI','https://www.youtube.com/channel/UCs_AZuYXi6NA9tkdbhjItHQ',1),
('Top 10 Technologies to Learn in 2021 | Trending Technologies in 2021 | Edureka','https://www.youtube.com/c/edurekaIN',2),
('i bought a DDoS attack on the DARK WEB (dont do this)','https://www.youtube.com/c/NetworkChuck',2),
('Raspberry Pi Explained in 100 Seconds','https://www.youtube.com/c/AngularFirebase',2),
('Programming tutorials','https://www.youtube.com/user/grafikarttv',3),
('Kubernetes Tutorial for Beginners [FULL COURSE in 4 Hours]','https://www.youtube.com/channel/UCdngmbVKX1Tgre699-XLlUA',1),
('LES BASES DE GIT (tuto débutant)','https://www.youtube.com/c/Gravenilvectuto/',3);