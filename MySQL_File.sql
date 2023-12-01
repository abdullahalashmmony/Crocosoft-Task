create table user
(
    UserID   int auto_increment
        primary key,
    UserName varchar(255) null,
    Email    varchar(255) null,
    constraint Email
        unique (Email)
);

create table follow_friendship
(
    RelationshipID int auto_increment
        primary key,
    UserID1        int null,
    UserID2        int null,
    constraint follow_friendship_ibfk_1
        foreign key (UserID1) references user (UserID),
    constraint follow_friendship_ibfk_2
        foreign key (UserID2) references user (UserID)
);

create index UserID1
    on follow_friendship (UserID1);

create index UserID2
    on follow_friendship (UserID2);

create table post
(
    PostID    int auto_increment
        primary key,
    UserID    int                                null,
    Content   text                               null,
    Timestamp datetime default CURRENT_TIMESTAMP null on update CURRENT_TIMESTAMP,
    constraint post_ibfk_1
        foreign key (UserID) references user (UserID)
);

create table comment
(
    CommentID int auto_increment
        primary key,
    PostID    int                                null,
    UserID    int                                null,
    Content   text                               null,
    Timestamp datetime default CURRENT_TIMESTAMP null on update CURRENT_TIMESTAMP,
    constraint comment_ibfk_1
        foreign key (PostID) references post (PostID),
    constraint comment_ibfk_2
        foreign key (UserID) references user (UserID)
);

create index PostID
    on comment (PostID);

create index UserID
    on comment (UserID);

create table `like`
(
    LikeID int auto_increment
        primary key,
    PostID int null,
    UserID int null,
    constraint like_ibfk_1
        foreign key (PostID) references post (PostID),
    constraint like_ibfk_2
        foreign key (UserID) references user (UserID),
    constraint like_ibfk_3
        foreign key (UserID) references `like` (PostID)
);

create index PostID
    on `like` (PostID);

create index UserID
    on `like` (UserID);

create index UserID
    on post (UserID);

create table share
(
    ShareID int auto_increment
        primary key,
    PostID  int null,
    UserID  int null,
    constraint share_ibfk_1
        foreign key (PostID) references post (PostID),
    constraint share_ibfk_2
        foreign key (UserID) references user (UserID)
);

create index PostID
    on share (PostID);

create index UserID
    on share (UserID);

