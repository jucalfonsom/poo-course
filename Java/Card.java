class Card extends Payment {
    Integer numberCard;
    String dateCard;
    String cvv;

    public Card(Integer id, String dateCard, String cvv){
        super(id);
        this.dateCard = dateCard;
        this.cvv = cvv;
    }
}