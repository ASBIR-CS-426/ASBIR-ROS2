#include <chrono>
#include <functional>
#include <memory>
#include <string>

#include "rclcpp/rclcpp.hpp"
#include "tf2/exceptions.h"
#include "tf2_ros/transform_listener.h"
#include "tf2_ros/buffer.h"

#include <std_msgs/msg/string.hpp>
#include <geometry_msgs/msg/point_stamped.hpp>

using namespace std;
using std::placeholders::_1;

class TransformPoint : public rclcpp::Node {
    public:
        TransformPoint() : Node("TransformPoint"), count_(0) {
            point_sub = this->create_subscription<geometry_msgs::msg::PointStamped>("point_to_transform", 10, std::bind(&TransformPoint::topic_callback, this, _1));
            point_pub = this->create_publisher<geometry_msgs::msg::PointStamped>("transformed_point", 10);
            tf_buffer = std::make_unique<tf2_ros::Buffer>(this->get_clock());
            tf_listener = std::make_shared<tf2_ros::TransformListener>(*tf_buffer);
            base_frame = "odom_frame";

        }
    private:
        void topic_callback(const std_msgs::msg::String::SharedPtr msg) const{
            // RCLCPP_INFO(this->get_logger(), "I heard: '%s'", msg->data.c_str());
            geometry_msgs::msg::PointStamped transformed_point = tf2::Transform(msg, base_frame);

        }
        rclcpp::Subscription<geometry_msgs::msg::PointStamped>::SharedPtr point_sub;
        rclcpp::Publisher<geometry_msgs::msg::PointStamped>::SharedPtr point_pub;
        std::shared_ptr<tf2_ros::TransformListener> tf_listener{nullptr};
        std::unique_ptr<tf2_ros::Buffer> tf_buffer;
        std::string base_frame;
        int count_;
};

int main(int argc, char * argv[])
{
  rclcpp::init(argc, argv);
  rclcpp::spin(std::make_shared<TransformPoint>());
  rclcpp::shutdown();
  return 0;
}