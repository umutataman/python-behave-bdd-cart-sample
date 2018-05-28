Feature: Challange gittigidiyor

  Scenario: Cart cases for televizyon and iphone
    Given I go to website "https://www.gittigidiyor.com"
    When I search for "televizyon"
      And I click page "2" and item "5"
      And I save price for "televizyon"
      And I click "Sepete Ekle" id "add-to-basket" without Fixpack
    Then I confirm television_price equals to cart_price
    Given I go to website "https://www.gittigidiyor.com"
    When I search for "iphone"
      And I click page "1" and item "5"
      And I save price for "iphone"
      And I click "Sepete Ekle" id "add-to-basket" without Fixpack
    Then I confirm total_price equals to tv plus iphone
    When I delete "televizyon"
    Then I confirm total_price equals to iphone
    When I clear Shopping Cart